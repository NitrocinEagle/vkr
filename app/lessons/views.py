from django.views.generic import TemplateView
from .models import Lesson
from app.answers.models import Answer
from app.user.mixins import UsernameMixin


class AllLessonsView(UsernameMixin, TemplateView):
    template_name = 'all_lessons.html'

    def get_context_data(self, **kwargs):
        kwargs['lessons'] = Lesson.objects.all()
        kwargs['answers'] = Answer.objects.filter(user=self.request.user)
        return super(AllLessonsView, self).get_context_data(**kwargs)


class OneLessonView(UsernameMixin, TemplateView):
    template_name = 'one_lesson.html'

    def get_context_data(self, **kwargs):
        kwargs['answer'] = Answer.objects.filter(lesson=kwargs['lesson_id'],
                                                 user=self.request.user).first()
        kwargs['lesson_id'] = kwargs['lesson_id']
        kwargs['lesson'] = Lesson.objects.get(id=kwargs['lesson_id'])
        return super(OneLessonView, self).get_context_data(**kwargs)
