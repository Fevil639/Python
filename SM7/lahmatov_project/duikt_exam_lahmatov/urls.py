from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('duikt_page_lahmatov')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect),
    path('', include('lahmatov_task.urls')),
]
