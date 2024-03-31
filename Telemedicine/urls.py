from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from Blood import views

urlpatterns = [
    path("",views.index,name='home'),
]