from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from app.lessons.models import Lesson
from app.test.models import TestCaseExample, TestCase, TestCasePass
from app.answers.models import Answer
from app.user.mixins import UsernameMixin
from .forms import UploadAnswerForm


class UploadAnswerFormView(UsernameMixin, FormView):
    template_name = 'file_upload.html'
    form_class = UploadAnswerForm

    def form_valid(self, form):
        tester = self.form_class
        lesson = Lesson.objects.get(id=self.kwargs['lesson_id'])
        upload_file_data = {
            'self': self,
            'file': self.request.FILES['answer_file'],
            'prefix': lesson.slug + '_' + self.request.user.username,
            'dir': settings.BASE_DIR
        }

        cpp_file = tester.handle_uploaded_file(**upload_file_data)
        test_passed = True
        for case in TestCase.objects.filter(lesson=self.kwargs['lesson_id']):
            make_test_data = {
                'self': self,
                'script': settings.MAKE_TEST_SCRIPT_FILE,
                'cpp': cpp_file,
                'input': case.input.path,
                'etalon': case.output_etalon.path,
                'base_dir': settings.BASE_DIR,
            }
            result = str(tester.make_test(**make_test_data))
            matched = True if len(result) == 0 else False
            test_passed *= matched
            test_case = TestCasePass.objects.filter(lesson=lesson,
                                                    user=self.request.user,
                                                    test=case)
            if test_case:
                test_case.update(passed=matched)
            else:
                TestCasePass(lesson=lesson, user=self.request.user, test=case,
                             passed=matched).save()
        answer_data = {
            'lesson': lesson,
            'user': self.request.user,
            'cpp_file': cpp_file,
            'test_pass': test_passed
        }
        answer = Answer.objects.filter(lesson=lesson,
                                       user=self.request.user)
        if answer:
            answer.update(test_pass=test_passed)
        else:
            Answer(**answer_data).save()
        return super(UploadAnswerFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['test'] = TestCaseExample.objects.get(
            lesson=self.kwargs['lesson_id'])
        return super(UploadAnswerFormView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('results:test_result',
                            kwargs={'lesson_id': self.kwargs['lesson_id']})
