from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/timeline/', include('admin_timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),

    
    url(r'^email/', 'www.views.sendemail'),
    url(r'^Contact/', 'www.views.view_contact_us'),
    # url(r'^test/', 'www.views.delete_post'),
    # url(r'^test1/', 'www.views.test1'),
    url(r'^base/', 'www.views.render_base'),
    url(r'^radio/', 'www.views.render_radioAds'),
    url(r'^add/video/', 'www.views.add_video'),
    url(r'^/weddingclips/', 'www.views.show_wedding_videos'),
    url(r'^/documentaryclips/', 'www.views.show_documentaries_videos'),
    url(r'^/promoclips/', 'www.views.show_promo_videos'),
    url(r'^add/contact/', 'www.views.add_contact'),
    url(r'^testincrement/', 'www.views.increment_number_of_views'),
)

urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^sorl/', 'www.views.render_app_test'),
)

