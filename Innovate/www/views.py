from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError
from www.models import *
from www.forms import *


def show_videos(request):
	list_of_videos = video.objects.all()
	return render_to_response('shortmovies.html',{'list_of_videos':list_of_videos})

#Abdelrahman Maged-This method get the form from the html. but first it checks whether 
#the request is post or not. if it is it checks whether the form is valid or not. if the
#form is valid it creates a new instance of the contact object. and then it redirects to add_contact.html with success variable.
#if the form is not valid it just refreshes the feed and shows the form blank again. 
def add_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print form.cleaned_data['telephonenumber']
			print form.cleaned_data['email']
			print form.cleaned_data['skypename']
			print form.cleaned_data['addressline1']
			print form.cleaned_data['addressline2']
			print form.cleaned_data['addressline3']

			contact.objects.create(
				telephone_number = form.cleaned_data['telephonenumber'],
				email = form.cleaned_data['email'],
				skype_name = form.cleaned_data['skypename'],
				address_line1 = form.cleaned_data['addressline1'],
				address_line2 = form.cleaned_data['addressline2'],
				address_line3 = form.cleaned_data['addressline3']
				)
			return render_to_response('add_contact.html',{'success':'true'})          
		else:
			return render_to_response('add_contact.html')
	else:
		form = ContactForm()
		context = {'form': form}
		return render_to_response('add_contact.html', context, context_instance=RequestContext(request))

#Abdelrahman Maged-This method get the form from the html. but first it checks whether 
#the request is post or not. if it is it checks whether the form is valid or not. if the
#form is valid it creates a new instance of the video object. and then it redirects to add_video.html with success variable.
#if the form is not valid it just refreshes the feed and shows the form blank again.
def add_video(request):
	if request.method == 'POST':
		form = VideoForm(request.POST)
		if form.is_valid():
			print form.cleaned_data['video_genre']
			video.objects.create(youtube_url = form.cleaned_data['youtube_url'],
				title = form.cleaned_data['title'],
				director = form.cleaned_data['director'],
				producer = form.cleaned_data['producer'],
				photographer = form.cleaned_data['photographer'],
				video_genre = form.cleaned_data['video_genre']
				)
			return render_to_response('add_video.html',{'success':'true'})          
		else:
			return render_to_response('add_video.html')
	else:
		form = VideoForm()
		context = {'form': form}
		return render_to_response('add_video.html', context, context_instance=RequestContext(request))


#Abdelrahman Maged-This method get the senderName, SenderEmail and SenderMessage from the POST request received from the contactus.html.
#to_email is retrieved from the most recent record in the contact table. Email will be sent and the page will redirected to the url confirm_send.
def sendemail(request):
	SenderName = request.POST['name']
	SenderEmail = request.POST['email']
	SenderMessage = request.POST['message']
	to_email = contact.objects.all()[contact.objects.all().count()-1].email
	send_mail('Complain by', SenderMessage, SenderEmail,
	['abdelrahman.maged@gmail.com'], fail_silently=False)
	send_mail('Thank You','Thank you for contacting us, note kindly that your message will be considered by one of our representatives and contact you shortly', 'test@test.com',[SenderEmail])
	return HttpResponseRedirect('/confirm_send/')

#Abdelrahman Maged-This method retrieves the most new contact object from the table
#and renders it the contactus.html
def view_contact_us(request):
	contact_obj = contact.objects.all()
	print contact_obj.count()-1
	contact_obj = contact_obj[contact_obj.count()-1]
	return render_to_response('contactus.html', {'contact_obj':contact_obj})

#Beshoy Atef-This Method render the Main Page for checking Perposes 
def render_base(request):
	return render_to_response('base.html',context_instance=RequestContext(request))

#Beshoy Atef-This Method render the Main Page for checking Perposes 
def render_radioAds(request):
	return render_to_response('radio.html',context_instance=RequestContext(request))

def test(request):
	link = 'http://www.youtube.com/watch?v=8t7fLDtgtuE'
	return render_to_response('test.html',{'link':link})