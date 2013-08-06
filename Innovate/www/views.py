from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError
from www.models import *
import soundcloud


#Abdelrahman Maged-This view will redirect the user to the deletevideo.html page.
def render_delete_video_page(request):
	return render_to_response('deletevideo.html')

#Abdelrahman Maged-This view will send a list of videos of the genre that the user selected.
def render_videos_to_be_deleted(request,category):
	print category
	data =  video.objects.filter(video_genre = category)
	return render_to_response('deletevideo.html',{'videos':data})

#Abdelrahman Maged-This view delete the video with the specific id.
def delete_video(request):
	video_id = request.POST['video']
	video.objects.get(pk=video_id).delete();
	return HttpResponse('')


def sendemail(request):
	SenderName = request.POST['name']
	SenderEmail = request.POST['email']
	SenderMessage = request.POST['message']
	to_email = contact.objects.all()[0].email
	send_mail('Complain by', SenderMessage, SenderEmail,
	['beshosmile@gmail.com'], fail_silently=False)
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
	radio_ads = radio_ad.objects.all()
	track_list = list()


	client = soundcloud.Client(client_id='dc93bd6c42e7e5d82a7718f2c8abf695')
	for ad in radio_ads:
		track = client.get('/resolve', url=ad.url)
		track_list.append(track.id)



	

	# print the html for the player widget
	# print embed_info
	# print embed_info['html']
	return render_to_response('radio.html', {'track_list':track_list},context_instance=RequestContext(request))