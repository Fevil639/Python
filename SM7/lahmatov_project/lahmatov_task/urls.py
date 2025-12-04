from django.urls import path
from . import views

urlpatterns = [
    path('install/', views.install, name='install'),
    path('duikt_page_lahmatov/', views.duikt_page_lahmatov, name='duikt_page_lahmatov'),
]
