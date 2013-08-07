from django.contrib import admin
from www.models import *
from django.forms.fields import Field
from django import forms
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from filer.models import Image    
from filer import settings as filer_settings
from filer_gallery.widgets import UploadWidget
from filer_gallery.utils import handle_upload, UploadException


class GalleryImageAdminInline(admin.TabularInline):
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    inlines = (GalleryImageAdminInline, )
    list_display = ('__unicode__', 'title')
    list_editable = ('title',) 
    prepopulated_fields = {'slug': ('title',) }
    


            
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','gallery', 'title', 'image')
    list_editable = ('title', 'image')
    list_filter = ('gallery',)

admin.site.register(video)
admin.site.register(contact)
admin.site.register(radio_ad)    
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(sorl_test)


