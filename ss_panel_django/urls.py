"""ss_panel_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^adminmgr/', include('adminmgr.urls')),
    url(r'^$','ss_panel_django.views.index' ,name='index'),
    url(r'^login$','users.views.login' ,name='login'),
    url(r'^register$','users.views.register' ,name='register'),
    url(r'^users/', include('users.urls')),
    url(r'^captcha/', include('captcha.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('', ('', include('django_evercookie.urls')),)
