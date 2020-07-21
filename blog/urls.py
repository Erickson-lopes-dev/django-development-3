from django.contrib import admin
from django.urls import path, include

from blog.view import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('', include("website.urls")),
]
