from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^registerForm$',views.registerForm,name='registerForm'),
    url(r'^loginForm$',views.loginForm,name='loginForm'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^updateUserInfo$',views.updateUserInfo,name='updateUserInfo'),
    url(r'^updateUserInfoForm$',views.updateUserInfoForm,name='updateUserInfoForm'),
    url(r'^updateSSPwdForm$',views.updateSSPwdForm,name='updateSSPwdForm'),
    
    url(r'^userCenter$',views.userCenter,name='userCenter'),
    
]