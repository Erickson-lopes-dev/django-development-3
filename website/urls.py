from django.urls import path
from .views import *

urlpatterns = [
    path('', hello_blog, name='posts'),
    path('post/<int:id>', post_detail, name='post_detail')
]
