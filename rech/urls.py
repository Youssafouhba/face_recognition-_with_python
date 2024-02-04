from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.rech,name="rech"),
    
]