from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def Index(request):
    send_mail('Hello from rasool','Hello there it is automatic msg.http://127.0.0.1:8000/login/','rasool.m7860@gmail.com',['djpython8022@gmail.com'],fail_silently=False)
    return render(request,'index.html')