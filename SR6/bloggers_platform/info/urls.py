from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    path('profiles/', views.profiles),
    re_path(r'^profiles/(?P<blogger_id>\d+)/$', views.profile_detail),
    path('news/', views.news),
]