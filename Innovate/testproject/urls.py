from django.conf.urls import patterns, include, url
from testproject import settings

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

    url(r'^email/', 'www.views.sendemail'),
    url(r'^upload/', 'www.views.add_album'),
    url(r'^pic/', 'www.views.upload_pic'),
    url(r'^Contact/', 'www.views.view_contact_us'),
    url(r'^all/', 'www.views.pictures'),
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





    


)

urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
