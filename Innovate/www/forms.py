
from www.models import *
from django import forms


class AlbumForm(forms.Form):
    title= forms.CharField(label="title")
    description = forms.CharField(label='description')
    event_date =  forms.DateField()
 


class PicForm(forms.Form):
	photo = forms.ImageField()
	albumid = forms.CharField(label='albumid',widget = forms.TextInput(attrs={'readonly': 'readonly '}))

class aboutusForm(forms.Form):
	title= forms.CharField(label="title")
	description = forms.CharField(label='description')
	photo = forms.ImageField()


# from django import forms.ValidationError
class VideoForm(forms.Form):
	youtube_url = forms.CharField(max_length='150', required=True)
	title = forms.CharField(max_length='150' ,required=True)
	director = forms.CharField(max_length='50',required=True)
	producer = forms.CharField(max_length='50',required=True)
	photographer = forms.CharField(max_length='50',required=True)
	video_cover = forms.ImageField(required=True)
	video_genre = forms.ChoiceField(widget = forms.Select(), 
					 choices = ([('w','wedding'), ('d','documentary'),('p','promos'), ]),required = True,)

class ContactForm(forms.Form):
	skypename = forms.CharField(max_length='50', required=True)
	telephonenumber = forms.CharField(max_length='50', required=True)
	addressline1 = forms.CharField(max_length='50', required=False)
	addressline2 = forms.CharField(max_length='50', required=False)
	addressline3 = forms.CharField(max_length='50', required=False)
	email = forms.CharField(max_length='50', required=True)


class PicForm(forms.Form):
	photo = forms.ImageField()

