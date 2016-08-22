from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^lawdb/', include('lawdb.urls')),
    url(r'^admin/', admin.site.urls),
]
