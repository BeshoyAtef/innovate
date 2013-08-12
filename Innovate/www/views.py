from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context,RequestContext, Context
from django import forms 
from www.forms import *
from www.models import*
from django.core.mail import send_mail, BadHeaderError
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


#Abdelrahman Maged- This method gets the video-id from the post request. then it retrieves
#the video object with the entered id and increment the number of views of it by one.
#it returns an empty httpresponse.
def increment_number_of_views(request):
	video_id = request.POST['video']
	video_obj = video.objects.get(pk=video_id)
	old_number_of_views = video_obj.number_of_views
	video_obj.number_of_views = old_number_of_views + 1
	video_obj.save()
	return HttpResponse('')

#Abdelrahman Maged-This view returns to the shortmovies.html a list of all the wedding videos.
def show_wedding_videos(request):
	list_of_videos = video.objects.filter(video_genre='W')
	print list_of_videos
	return render_to_response('shortmovies.html',{'list_of_videos':list_of_videos, 'wedding':'wedding'})

#Abdelrahman Maged-This view returns to the shortmovies.html a list of all the documentary videos.
def show_documentaries_videos(request):
	list_of_videos = video.objects.filter(video_genre='D')
	return render_to_response('shortmovies.html',{'list_of_videos':list_of_videos,'doc':'doc'})

#Abdelrahman Maged-'This video returns to the shortmovies.html a list of all promo videos'
def show_promo_videos(request):
	list_of_videos = video.objects.filter(video_genre='P')
	return render_to_response('shortmovies.html',{'list_of_videos':list_of_videos,'promo':'promo'})

#Abdelrahman Maged-This method get the form from the html. but first it checks whether 
#the request is post or not. if it is it checks whether the form is valid or not. if the
#form is valid it creates a new instance of the contact object. and then it redirects to add_contact.html with success variable.
#if the form is not valid it just refreshes the feed and shows the form blank again. 
def add_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
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
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			print form.cleaned_data['video_cover']
			video.objects.create(youtube_url = form.cleaned_data['youtube_url'],
				title = form.cleaned_data['title'],
				director = form.cleaned_data['director'],
				producer = form.cleaned_data['producer'],
				photographer = form.cleaned_data['photographer'],
				video_genre = form.cleaned_data['video_genre'],
				video_cover = form.cleaned_data['video_cover']
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
	['beshosmile@gmail.com'], fail_silently=False)
	send_mail('Thank You','Thank you for contacting us, note kindly that your message will be considered by one of our representatives and contact you shortly', 'test@test.com',[SenderEmail])
	return HttpResponseRedirect('/confirm_send/')

#Abdelrahman Maged-This method retrieves the most new contact object from the table
#and renders it the contactus.html
def view_contact_us(request):
	contact_obj = contact.objects.all()
	print contact_obj.count()-1
	contact_obj = contact_obj[contact_obj.count()-1]
	return render_to_response('contactus.html', {'contact_obj':contact_obj})


#Beshoy Atef-This Method render the Main  for checking Perposes 
def render_main(request):
	main_page_obj = main_page.objects.get(pk=1)
	thumbnails=main_page_moviestrip.objects.filter(main_page=main_page_obj)
	return render_to_response('index.html',{'main_page':main_page,'thumbnails':thumbnails},context_instance=RequestContext(request))


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

#Beshoy Atef-This Method render the sorl test Page for checking Perposes 
def render_app_test(request):
	imgs = sorl_test.objects.all()
	img = 0
	if imgs:
		img = imgs[0]
	return render_to_response('test.html',{'thumb':imgs},context_instance=RequestContext(request))


#Beshoy Atef-This Method render the Main Page for checking Perposes 
def render_radioAds(request):
	return render_to_response('radio.html',context_instance=RequestContext(request))

def test(request):
	link = 'http://www.youtube.com/watch?v=8t7fLDtgtuE'
	return render_to_response('test.html',{'link':link})
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
	abouts = AboutUs.objects.all()
	about=abouts[0]
	print about
	return render_to_response('about.html',{'about':about})

