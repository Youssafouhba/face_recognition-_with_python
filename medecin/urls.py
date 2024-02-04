from django.urls import path
from . import views

urlpatterns=[

    path('',views.medecin,name='medecin'),

    path('suivant',views.suivant,name='suivant'),

    path('deconnect',views.deconnect,name='deconnect'),
    
]