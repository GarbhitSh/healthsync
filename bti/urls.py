from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


# btiapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_image, name='index'),
]
