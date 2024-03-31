# Xray/urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    
    path('', views.home, name='index'),
    path('result/', views.result, name='result'),
    path('rules/', views.show_rules, name='rules'),
    path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
