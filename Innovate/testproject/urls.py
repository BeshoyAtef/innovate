from django.conf.urls import patterns, include, url
from testproject import settings

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
    url(r'^admin/timeline/', include('admin_timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),

    
    url(r'^upload/', 'www.views.add_album'),
    url(r'^pic/', 'www.views.upload_pic'),
    url(r'^Contact/', 'www.views.view_contact_us'),
    url(r'^picc/', 'www.views.Albumshow'),
    url(r'^cover/', 'www.views.albumpic'),
    url(r'^showpic/', 'www.views.picshow'),
    url(r'^albumcover/', 'www.views.cover'),
    url(r'^aboutus/', 'www.views.aboutuspage'),
    url(r'^deleteAlbum/', 'www.views.renderalbum'),
    url(r'^albumdelete/', 'www.views.delete_album'),
    url(r'^albumshow/', 'www.views.album_pic'),
    url(r'^deletepic/', 'www.views.render_pic'),
    url(r'^deleted/', 'www.views.delete_pic'),
    # url(r'^wedding/', 'www.views.albums_gal'),
    url(r'^gallery/', 'www.views.weddinggallery'),
    url(r'^about/', 'www.views.aboutusrendering'),

    url(r'^base/', 'www.views.render_base'),

    #beshoy renders-front end related urls
    url(r'^sorl/', 'www.views.render_app_test'),
    url(r'^base/', 'www.views.render_base'),
    url(r'^radio/', 'www.views.render_radioAds'),
    url(r'^$', 'www.views.render_main',name='home'),


    # abdos renders-front end related urls
    url(r'^weddingclips/', 'www.views.show_wedding_videos'),
    url(r'^documentaryclips/', 'www.views.show_documentaries_videos'),
    url(r'^promoclips/', 'www.views.show_promo_videos'),

    # abdo's functions-bk end related urls
    url(r'^email/', 'www.views.sendemail'),
    url(r'^Delete/Video/(?P<category>\w+)/$', 'www.views.render_videos_to_be_deleted'),
    url(r'^confirmdelete/', 'www.views.delete_video'),
    url(r'^Delete/', 'www.views.render_delete_video_page'),
    url(r'^base/', 'www.views.render_base'),
    url(r'^add/video/', 'www.views.add_video'),
    url(r'^add/contact/', 'www.views.add_contact'),
    url(r'^testincrement/', 'www.views.increment_number_of_views'),
    # url(r'^p/(?P<num>\d+)/$', 'blog.views.page'),
    url(r'^p/(?P<category>\w+)/$', 'www.views.albums_gal'),
    url(r'^t/(?P<category>\w+)/$', 'www.views.landing_page'),
    url(r'^google4b6c7ff943e0c6ed.html', 'www.views.googlecheck'),
    


)
urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
