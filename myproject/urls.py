"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #url(r'^', 'vkr.views.index'),
    url(r'^admin/', admin.site.urls),
    url(r'^theory/all/$', 'vkr.views.index'),
    url(r'^theory/all/lesson/(?P<theory_id>\d+)/$', 'vkr.views.oneTheory'),
    url(r'auth/', include('loginsys.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # TODO попробовать сделать переход по слагу, а не id
    # TODO сделать домашнюю страницу, навести порядок в urls и views
    # url(r'^', 'vkr.urls'),
]
