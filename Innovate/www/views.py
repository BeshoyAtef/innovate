from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext, Context

from django.core.mail import send_mail, BadHeaderError
from www.models import *
def sendemail(request):
	SenderName = request.POST['name']
	SenderEmail = request.POST['email']
	SenderMessage = request.POST['message']
	to_email = contact.objects.all()[0].email
	send_mail('Complain by', SenderMessage, SenderEmail,
	['abdelrahman.maged@gmail.com'], fail_silently=False)
	send_mail('Thank You','Thank you for contacting us, note kindly that your message will be considered by one of our representatives and contact you shortly', 'test@test.com',[SenderEmail])
	return HttpResponseRedirect('/confirm_send/')

def view_contact_us(request):
	contact_obj = contact.objects.all()
	contact_obj = contact_obj[0]
	return render_to_response('contactus.html', {'contact_obj':contact_obj})

#Beshoy Atef-This Method render the Main Page for checking Perposes 
def render_base(request):
	return render_to_response('base.html',context_instance=RequestContext(request))

#Beshoy Atef-This Method render the Main Page for checking Perposes 
def render_radioAds(request):
	return render_to_response('radio.html',context_instance=RequestContext(request))