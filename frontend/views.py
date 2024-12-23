from django.shortcuts import render,get_object_or_404
from dashboard.models import post
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

import threading

def index(request):
    posts = post.objects.order_by('-created_at')[:3]
    return render(request, 'f_index.html',{'posts':posts})

def post_detail(request, slug):
    posts = get_object_or_404(post, slug=slug)
    return render(request, 'innernews.html', {'posts': posts})

def send_email(subject, message, from_email, recipient_list, fail_silently=False):
    print(f'\n--Another thread created for sending bulk mail\n---')
    print(f'\nmail sent to: {recipient_list}\n')
    send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently)


def bulkmail(request):
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        email=request.POST['email']
        email_list= email.split(",")

        # send_mail(subject,message,settings.EMAIL_HOST_USER,email_list,fail_silently=False)
        email_thread = threading.Thread(target=send_email, args=(subject, message, settings.EMAIL_HOST_USER, email_list, False))
        email_thread.start()
        messages.success(request,'Email sent successfully')
        # return redirect('bulkmail') 
    
    return render(request,'bulkEmailForm.html')