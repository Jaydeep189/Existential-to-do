from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('todo', views.todo, name="todo"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('', views.index, name="home"),
    path('proc', views.proc)
]
