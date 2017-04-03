from django.conf.urls import include, url
from django.contrib import admin

from cow import urls as cow_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include(cow_urls)),
]
