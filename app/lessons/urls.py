from django.conf.urls import url
from .views import AllLessonsView, OneLessonView

urlpatterns = [
    url(r'^$', AllLessonsView.as_view(), name='index'),
    url(r'^lesson/(?P<lesson_id>\d+)/$', OneLessonView.as_view(), name='lesson'),
]
