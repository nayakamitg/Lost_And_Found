from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('add_person/', views.add_person,name="add_person" ),
    path('details/<int:sno>/', views.detail,name="Details" ),
    path('edit/<int:sno>/', views.edit,name="edit" ),
]
