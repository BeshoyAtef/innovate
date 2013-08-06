from django.db import models

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

