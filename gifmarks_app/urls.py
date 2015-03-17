from django.conf.urls import patterns, url
from gifmarks_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_a_gif, name='add_a_gif'),
    url(r'^(?P<gif_id>\d+)/$', views.show_a_gif, name='show_a_gif'),
)
