from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gifmarks_app.views.index', name='index'),

    url(r'^gif/', include('gifmarks_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
