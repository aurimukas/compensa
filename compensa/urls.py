from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'com_local.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^compensa/', include('com_local.urls', namespace='com_local')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
