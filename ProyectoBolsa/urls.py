"""ProyectoFiltrosUPNA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #Paths AppCore
    path('', include('AppCore.urls')),
    #Paths Checks
    path('checks/', include('AppCheckCeleryChannels.urls')),
    #Path del admin
    path('admin/', admin.site.urls),
    #Paths AppAccounts
    path('accounts/', include('AppAccounts.urls')),
    #Paths AppContacto
    path('contacto/', include('AppContacto.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)