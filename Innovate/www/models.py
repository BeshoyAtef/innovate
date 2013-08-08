from django.db import models
from django.utils.timezone import utc
import datetime
from datetime import timedelta
# Create your models here.

#album table defines elements of the ablum with the title,descr and date of the pictures regarding that album
class Album(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500, null=True)
	event_date = models.DateField(null=True)


#table pics defines the pictures regarding one ablum (no limit)
class Pictures(models.Model):
    picture1 = models.ImageField(upload_to='media', blank=True)
    album = models.ForeignKey(Album)


class AblumCover(models.Model):
	picture = models.ForeignKey(Pictures)
	album = models.ForeignKey(Album)

class AboutUs(models.Model):
	title1=models.CharField(max_length=50)
	description1=models.CharField(max_length=700)
	picture1 = models.ImageField(upload_to='media')
	title2=models.CharField(max_length=50)
	description2=models.CharField(max_length=700)
	picture2 = models.ImageField(upload_to='media')
	title3=models.CharField(max_length=50)
	description3=models.CharField(max_length=700)
	picture3 = models.ImageField(upload_to='media')
	title4=models.CharField(max_length=50)
	description4=models.CharField(max_length=700)
	picture4 = models.ImageField(upload_to='media')


class video(models.Model):
	youtube_url = models.CharField(max_length='150')
	video_cover = models.ImageField(upload_to='media')
	title = models.CharField(max_length='150')
	director = models.CharField(max_length='50')
	producer = models.CharField(max_length='50')
	photographer = models.CharField(max_length='50')
	number_of_views = models.IntegerField(default='0')
	video_choices = (
		('W', 'Wedding'),
		('P', 'Promo'),
		('D', 'Documentaries'),
	)
	video_genre = models.CharField(max_length=1, choices=video_choices)

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




class sorl_test(models.Model):
	image=models.ImageField(upload_to='testsorl')

