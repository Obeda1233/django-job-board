from django.shortcuts import render
from .models import info
# Create your views here.
def send_message(request):
    myinfo = info.objects.first
    if request.method =='POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
    return render (request,'contact/contact.html',{'myinfo':myinfo})