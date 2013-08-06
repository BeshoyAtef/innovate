from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from www import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    # url(r'^users/profile/', 'render_videos_to_be_deleted'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^email/', 'www.views.sendemail'),
    url(r'^Contact/', 'www.views.view_contact_us'),
    url(r'^base/', 'www.views.render_base'),
    url(r'^Delete/Video/(?P<category>\w+)/$', 'www.views.render_videos_to_be_deleted'),
    url(r'^confirmdelete/', 'www.views.delete_video'),
    url(r'^Delete/', 'www.views.render_delete_video_page'),
    url(r'^base/', 'www.views.render_base'),
    url(r'^radio/', 'www.views.render_radioAds'),



)
urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )