from django.urls import path
from . import views

urlpatterns = [
    
    path('Crear_Chat/', views.Check_Channels_Celery, name='name-PruebaChat'),
    
]

