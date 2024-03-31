from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
   
    path("testimonial",views.testimonial,name='testimonial'),
    path("Blog",views.Blog,name='Blog'),
    path("project",views.project,name='project'),
    path("feature",views.feature,name='feature'),
    path("contact",views.contact,name='contact'),
    #path("about",views.about,name='about'),



    


    path("signup",views.signup,name='signup'),
    path("login",views.LoginPage,name='login'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("Doctor",views.Doctor,name='Doctor'),
    path("sb",views.sb,name='sb'),
   
    
]

