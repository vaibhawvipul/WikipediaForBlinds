from django.conf.urls import patterns, include, url
from livecode.helpgit import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'livecode.helpgit.views.user_login', name='user_login'),
    url(r'^logout/', 'livecode.helpgit.views.user_logout', name='user_logout'),
    url(r'^new/$', 'livecode.helpgit.views.new', name='new'),
    url(r'^search/$', 'livecode.helpgit.views.search', name='search'),
    url(r'^about/', 'livecode.helpgit.views.about', name='about'),
    url(r'^register/', 'livecode.helpgit.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
