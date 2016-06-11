from django.conf.urls import url
from .views import TestResultView

urlpatterns = [
    url(r'^(?P<lesson_id>\d+)/$', TestResultView.as_view(), name='test_result'),
]
