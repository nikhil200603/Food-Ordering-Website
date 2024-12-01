from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User=get_user_model()

@login_required(login_url='/login/')
def receipes(request):
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES['receipe_image']

        Receipe.objects.create(receipe_image=receipe_image,receipe_description=receipe_description,receipe_name=receipe_name)

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        return redirect('/receipe/')

    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))
        print(request.GET.get('search'))

    context={'receipes':queryset}    
    return render(request,'receipe.html',context)

@login_required(login_url='/login/')
def delete_receipe(request,id):
    query_set=Receipe.objects.get(id=id)
    query_set.delete()
    return redirect('/receipe/')

@login_required(login_url='/login/')
def update_receipe(request,id):
    query_set=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES['receipe_image']

        query_set.receipe_name=receipe_name
        query_set.receipe_description=receipe_description
        
        if receipe_image:
            query_set.receipe_image=receipe_image

        query_set.save()

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        return redirect('/receipe/')

    context={"receipe":query_set}
    return render(request,'update_receipe.html',context)

def login_page(request):
    if request.method=='POST':
        data=request.POST
        username=data.get('user_name')
        password=data.get('password')

        user=User.objects.filter(username = username)

        if not user.exists():
            messages.info(request,"Username doesnot exist")
            return redirect('/login/')

        user=authenticate(username=username,password=password)  

        if(user is None):
            messages.info(request,"Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipe/')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method=='POST':
        data=request.POST
        
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('user_name')
        password=data.get('password')

        user=User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "UserName already Taken")
            return redirect('/register/')

        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)    
        user.save()
        messages.info(request,"Account created Successfully")
        return redirect('/register/')

     
    return render(request,'register.html')

from django.db.models import Q,Sum    

def get_students(request):
    queryset=Student.objects.all()

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(deparment__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)
        )


    paginator = Paginator(queryset, 20)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'reports/students.html', {"queryset": page_obj})

from .seeds import *
def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id = student_id)  
    totalmarks=queryset.aggregate(total_marks=Sum('marks'))


    return render(request,'reports/marks.html',{'queryset':queryset,'total_marks':totalmarks,})

# Create your views her