from django.db import models

class contact(models.Model):
	email = models.CharField(max_length='100')
	address_line1 = models.CharField(max_length='100')
	address_line2 = models.CharField(max_length='100')
	address_line3 = models.CharField(max_length='100')
	skype_name = models.CharField(max_length='50')
	telephone_number = models.CharField(max_length='100')

class radio_ad(models.Model):
	title=models.CharField(max_length='500')
	url = models.TextField(max_length='1000')
	def __unicode__(self):
	    return self.title



from filer.fields.image import FilerImageField
from datetime import datetime
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField(default=datetime.now)
  
    def __unicode__(self):
        return self.title
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now)
    image = FilerImageField()

    def __unicode__(self):
            return self.title

class sorl_test(models.Model):
	image=models.ImageField(upload_to='testsorl')

