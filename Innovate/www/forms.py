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

