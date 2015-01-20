from django.conf.urls import patterns, url
from ToDoList import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))