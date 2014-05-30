from django.conf.urls import patterns, url
from xp_tracker_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_story/$', views.new_story, name='new_story'),
    url(r'^new_task/$', views.new_task, name='new_task')
)
