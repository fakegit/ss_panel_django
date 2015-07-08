from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adminLoginForm$',views.adminLoginForm,name='adminLoginForm'),
    url(r'^nodeEdit$',views.nodeEdit,name='nodeEdit'),
    url(r'^userMgr$',views.userMgr,name='userMgr'),
    url(r'^adminLogout$',views.adminLogout,name='adminLogout')
]
