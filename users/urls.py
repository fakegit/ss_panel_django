from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^registerForm$',views.registerForm1,name='registerForm'),
    url(r'^loginForm$',views.loginForm,name='loginForm'),
]