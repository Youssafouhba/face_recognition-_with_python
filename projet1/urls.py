from django.contrib import admin

from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('authentification.urls')),

    path('ajouter/', include('ajouter.urls')),

    path('medecin/',include('medecin.urls')),

    path('recup_infos/', include('recup_infos.urls')),

    path('face/', include('face.urls')),

    path('sec/', include('sec.urls')),

    path('rech/', include('rech.urls')),
]
