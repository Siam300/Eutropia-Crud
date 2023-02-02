from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('',views.show),
    path('nws',views.nws),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]