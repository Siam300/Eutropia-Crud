from django.contrib import admin
from django.urls import path
from news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.show),
    path('nws',views.nws),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)