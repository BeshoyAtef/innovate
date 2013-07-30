from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext, Context

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