from django.shortcuts import render
from django.http import HttpResponse


def hello_blog(request):
    return render(request, 'index.html')
