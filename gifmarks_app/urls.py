from django.conf.urls import patterns, url
from gifmarks_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<gif_id>\d+)/$', views.show_a_gif, name='show_a_gif'),
)
