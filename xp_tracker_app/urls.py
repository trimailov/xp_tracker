from django.conf.urls import patterns, url
from xp_tracker_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
