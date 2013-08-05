from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.template import RequestContext, Context
from django import forms 
from www.forms import *
from www.models import*
from django.core.mail import send_mail, BadHeaderError

def sendemail(request):
    SenderName = request.POST['name']
    SenderEmail = request.POST['email']
    SenderMessage = request.POST['message']
    send_mail('Complain by', SenderMessage, SenderEmail,
    ['abdelrahman.maged@gmail.com'], fail_silently=False)
    send_mail('Thank You','Thank you for contacting us, note kindly that your message will be considered by one of our representatives and contact you shortly', 'test@test.com',[SenderEmail])
    return HttpResponseRedirect('/confirm_send/')
def view_contact_us(request):
    return render_to_response('contactus.html')



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
	print albumid
	pic = Pictures.objects.filter(album_id=albumid)
	print pic
	return render_to_response('cover.html',{'pic':pic })

def albumpic(request):
	album = Album.objects.all()
	return render_to_response('cover.html',{'album':album})

def cover(request):
	picid = request.GET['picture']
	picobj = Pictures.objects.get(pk=picid)
	albumid = picobj.album_id
	if albumid is not None:
		if picid is not None:
			cover_pic = AblumCover.objects.create(picture_id=picid, album_id = albumid)
			cover_pic.save()
			return HttpResponse("done")


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









