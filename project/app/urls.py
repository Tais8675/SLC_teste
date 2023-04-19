from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name="index"),
    path("<int:app_id>", views.app, name="app"),
   
    
]
