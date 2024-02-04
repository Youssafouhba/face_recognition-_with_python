from django.urls import path,include
from . import views

urlpatterns = [

    path('recherche', views.recherche, name='recherche'),

    path('recherche_detect', views.recherche_detect, name='recherche_detect'),
    
    path('liste_attente', views.liste_attente, name='liste_attente'),
    
]