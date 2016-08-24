from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^$', auth_views.login),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^lawdb/', include('lawdb.urls')),
    url(r'^admin/', admin.site.urls),
]
