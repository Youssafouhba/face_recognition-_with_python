from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Dataset,name="face"),
    path('training',views.training,name="training"),
    path('detection',views.detection,name="detection"),
]