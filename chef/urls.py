from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.chef, name="chef"),
]