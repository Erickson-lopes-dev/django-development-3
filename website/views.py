from django.shortcuts import render
from django.http import HttpResponse


def hello_blog(request):
    lista = ['django', 'python', 'git', 'HTML', 'linux', 'Nginux', 'Banco de dados',  'Systemctl']
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
