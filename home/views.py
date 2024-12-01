from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_with_attachment
from django.conf import settings
from .models import *
import random

def home(request):
    car.objects.create(car_name=f"Nexon-{random.randint(0,100)}")
    #pass HTML
    # return HttpResponse("""
    #                     <h1>Hey I am Django Server</h1>
    #                     <p> Hey, I am from Django Sever</p>
    #                     <hr>
    #                     <br>
    #                     <p> Hey</p>""")
    
    peoples=[
        {'name':'Nikhil Kasaundhan','age':22},
        {'name':'Rohit Sharma','age':23},
        {'name':'Pulkit Verma','age':24},
        {'name':'Ishant Yadav','age':16},
        {'name':'Deepti Gupta','age':18},   
    ]
    vegetables=["Potato","Tomato","Raddish"]

    return render(request,"homes/index.html",context={'page':'Django 2024','peoples':peoples,'vegetables':vegetables})

def send_email(request):
    subject="This is the mail with Attachment"
    message="This mail contains a file Enjoy"
    recipient_list=['nikhilkasaundhan1@gmail.com','nikhilkasaundhan@gmail.com']
    file_path=f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachment(subject,message,recipient_list,file_path)
    return redirect('/')


def about(request):
    context={'page' : 'About'}
    return render(request,"homes//about.html",context)

def contact(request):
    context={'page' : 'Contact'}
    return render(request,"homes/contact.html",context)


def success_page(request):
    print("Just trying print")
    return HttpResponse("<h1>Hey,This is the succes page</h1>")

# Create your views here.
