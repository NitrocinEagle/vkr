from django.views.generic import TemplateView
from .models import Answer
from app.test.models import TestCasePass
from app.lessons.models import Lesson
from app.user.mixins import UsernameMixin


class TestResultView(UsernameMixin, TemplateView):
    template_name = 'test_results.html'

    def get_context_data(self, **kwargs):
        kwargs['answer'] = Answer.objects.filter(lesson=kwargs['lesson_id'],
                                                 user=self.request.user).first()
        kwargs['tests_results'] = TestCasePass.objects.filter(
            lesson=kwargs['lesson_id'],
            user=self.request.user)
        kwargs['lesson'] = Lesson.objects.get(id=kwargs['lesson_id'])
        return super(TestResultView, self).get_context_data(**kwargs)
