from django.conf.urls import url
from django.contrib import admin
from zappa_django_hello_world import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', views.index),
]
