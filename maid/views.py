from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Service

# Create your views here.

def index(request):
     services=Service.objects.all()
     return render(request,'frontend/index.html',{'services':services})

def register(request):
     return render(request,'frontend/register.html')

def navs(request):
     return render(request,'frontend/navs.html')

def loginfrom(request):
     return render(request,'frontend/login.html')

def addregister(request):
     email=request.POST['email']
     firstname=request.POST['firstname']
     lastname=request.POST['lastname']
     username=request.POST['username']
     password=request.POST['password']
     confirmpassword=request.POST['confirmpassword']

     if password==confirmpassword:
          if User.objects.filter(username=username).exists():
               messages.info(request,'Username มีคนใช้เเล้ว')
               return redirect('/register/')
          elif User.objects.filter(email=email).exists():
               messages.info(request,'Email นี้มีคนลงทะเบียนเเล้ว')
               return redirect('/register/')
          else :
               user=User.objects.create_user(
               username=username,
               password=password,
               email=email,
               first_name=firstname,
               last_name=lastname,
               )
               user.save()
               return redirect('/')
     else :
          messages.info(request,'รหัสผ่านไม่ตรงกัน')
          return redirect('/register/')


def login(request):
     username=request.POST['username']
     password=request.POST['password']

     #ckeck login
     user=auth.authenticate(username=username,password=password)

     if user is not None :
          auth.login(request,user)
          return redirect('/')
     else :
          messages.info(request,'ไม่พบข้อมูล')
          return redirect('/loginfrom/')

def service(request):
     return render(request,'frontend/service.html')

def index_Cleaning(request):
     return render(request,'frontend/index_Cleaning.html')

def index_Eliminate(request):
     return render(request,'frontend/index_Eliminate.html')

def index_Ironing(request):
     return render(request,'frontend/index_Ironing.html')

def index_landscaping(request):
     return render(request,'frontend/index_landscaping.html')

def index_Massage(request):
     return render(request,'frontend/index_Massage.html')

def index_Pool(request):
     return render(request,'frontend/index_Pool.html')

