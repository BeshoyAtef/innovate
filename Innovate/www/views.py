from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.template import RequestContext, Context
from django import forms 
from www.forms import *
from www.models import*
from django.core.mail import send_mail, BadHeaderError
from www.models import *
import soundcloud

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



def add_album(request):

	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			album = Album.objects.create(title = form.cleaned_data['title'], description= form.cleaned_data['description'],event_date=form.cleaned_data['event_date'])
			return HttpResponseRedirect('/picc/')
		else:
			return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = AlbumForm()
		context = {'form': form}
		return render_to_response('upload.html', context, context_instance=RequestContext(request))

def upload_pic(request):
	# albumid = request.GET['album']

	if request.method == 'POST': # If the form has been submitted...
		albumid = request.POST['albumid']
		if albumid is not None: 
			form = PicForm(request.POST, request.FILES)
			albumid = request.POST['albumid'] 
			if form.is_valid(): # All validation rules pass
				pic = Pictures(picture1= form.cleaned_data['photo'], album = Album.objects.get(pk=albumid))
				pic.save()
				return render_to_response('pic.html', {'pic': pic , 'form':form , 'upload':'true'}, context_instance=RequestContext(request))
				

			
			else:
				form = PicForm() # An unbound form

	else: 
    #add our registration form to context
		albumid=request.GET.get('albumid','');
		form = PicForm(initial={'albumid': albumid })
		return render_to_response('pic.html', {'form': form ,'upload':'true'})

def Albumshow(request):
	album = Album.objects.all()
	return render_to_response('pic.html', {'album':album ,'selectingAlbum':'true'})

def picshow(request):
	albumid= request.GET['albumid']
	pic = Pictures.objects.filter(album_id=albumid)
	return render_to_response('cover.html',{'pic':pic })

def albumpic(request):
	album = Album.objects.all()
	return render_to_response('cover.html',{'album':album})

def cover(request):
	picid = request.GET['picture']
	picobj = Pictures.objects.get(pk=picid)
	albumid = picobj.album_id
	if AblumCover.objects.filter(album_id=albumid).exists():
		AblumCover.objects.get(album_id = albumid).delete()
		AblumCover.objects.create(album_id=albumid,picture_id=picid)
		return HttpResponse('success')
	else:
		AblumCover.objects.create(album_id=albumid,picture_id=picid)
		return HttpResponse('success')


def aboutuspage(request):
	if request.method == 'POST':
		form = aboutusForm(request.POST, request.FILES)
		if form.is_valid():
			about = AboutUs.objects.create(title = form.cleaned_data['title'], description= form.cleaned_data['description'],picture=form.cleaned_data['photo'])
			about.save()
			return HttpResponse('information added')
		else:
			
			return render_to_response('aboutus.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = aboutusForm()
		context = {'form': form}
		return render_to_response('aboutus.html', context, context_instance=RequestContext(request))


def renderalbum(request):
	album = Album.objects.all()
	return render_to_response('deleteAlbum.html',{'album':album})




# def deletealbum(request):
# 	album = renderalbum(request)
# 	return render_to_response('deleteAlbum.html',{'album':album})
# 	print "im here "
# 	selectedalbum = request.GET['albumid']
# 	print selectedalbum
# 	if selectedalbum is not None:
# 		thealbum = Album.objects.get(pk=selectedalbum)
# 		thealbum.delete()
# 		return HttpResponse ("album has been delete")


def delete_album(request):
	albumid = request.POST['albumid']
	print albumid
	thealbum = Album.objects.get(pk=albumid)
	thealbum.delete()
	return HttpResponse("deleted")

def album_pic(request):
	album = Album.objects.all()
	return render_to_response('albumshow.html',{'album':album})

def render_pic(request):
	albumid= request.GET['albumid']
	print albumid
	pic = Pictures.objects.filter(album_id=albumid)
	print pic
	return render_to_response('deletepic.html',{'pic':pic })

def delete_pic(request):
	picid = request.GET['picture']
	pic = Pictures.objects.get(pk=picid)
	if picid is not None:
		delete_pic = Pictures.objects.get(pk=picid)
		delete_pic.delete()
		return HttpResponse("done")











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

def albums_gal(request):
	album = AblumCover.objects.all()
	return render_to_response('wedding.html', {'album':album})

def weddinggallery(request):
	print "imhere"
	albumid = request.GET['album']
	print albumid
	picture = Pictures.objects.filter(album_id=albumid)
	print picture
	return render_to_response('gallery.html',{'picture':picture})

def aboutusrendering(request):
	about = AboutUs.objects.all()
	print about
	return render_to_response('about.html',{'about':about})