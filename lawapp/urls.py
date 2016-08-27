from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', include('lawdb.urls')),
    url(r'lawdb/', include('lawdb.urls')),
]
