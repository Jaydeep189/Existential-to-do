from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('todo', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('', views.home, name="home"),
    path('proc', views.proc)
]
