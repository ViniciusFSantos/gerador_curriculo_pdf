from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin@gestao/', admin.site.urls),
    path('', include('core.urls')),
]
