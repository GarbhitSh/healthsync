from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
import datetime
#from . forms import createuserform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page.")


# Create your views here.
def index(request):

 return render(request,'index.html')


def about(request):
    return render(request,'about.html')   

def contact(request):
    return render(request,'contact.html')


def feature(request):
    return render(request,'feature.html')

def project(request):
    return render(request,'project.html')

def testimonial(request):
    return render(request,'testimonial.html')
def services(request):
    return render(request,'services.html')
def Blog(request):
    return render(request,'blog.html')


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')

def Doctor(request):
    return render(request,'doctor.html')
def sb(request):
    return render(request,'single-blog.html')