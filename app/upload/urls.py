from django.conf.urls import url
from .views import UploadAnswerFormView

urlpatterns = [
    url(r'(?P<lesson_id>\d+)$', UploadAnswerFormView.as_view(), name='index'),
]