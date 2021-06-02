
from django.urls import include, path
from hello import views

URLPattern = [
    path("", views.home, name = "home"),
    
    ]
