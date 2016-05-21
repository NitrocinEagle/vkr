from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
]