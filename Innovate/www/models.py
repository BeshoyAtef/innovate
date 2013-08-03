from django.db import models

class contact(models.Model):
	email = models.CharField(max_length='100')
	address_line1 = models.CharField(max_length='100')
	address_line2 = models.CharField(max_length='100')
	address_line3 = models.CharField(max_length='100')
	skype_name = models.CharField(max_length='50')
	telephone_number = models.CharField(max_length='100')

class main_page(models.Model):
	title=models.CharField(max_length='100')
	logo=models.ImageField(upload_to='mainpage')
	lens=models.ImageField(upload_to='mainpage')
	slogan=models.CharField(max_length='100')
	is_active=models.BooleanField(default=False)
	def __unicode__(self):
	    return str(self.id)+":"+self.title

class main_page_moviestrip(models.Model):
	main_page = models.ForeignKey(main_page)
	image=models.ImageField(upload_to='mainpage/moviestrip')
	title=models.CharField(max_length='100')
	def __unicode__(self):
	    return self.title