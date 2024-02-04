from django.urls import path
from .templates import views

urlpatterns = [
    
   path('', views.sec, name='sec'),
   path('recherche', views.recherche, name='recherche'),
    
]
