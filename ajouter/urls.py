from django.urls import  path
from . import views

urlpatterns = [
    path('',views.ajouter,name="ajouter"),
    path('ajout', views.ajout, name='ajout'),

]