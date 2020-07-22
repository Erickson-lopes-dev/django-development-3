from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    lista = ['django', 'python', 'git', 'HTML', 'linux', 'Nginux', 'Banco de dados', 'Systemctl']
    list_posts = Post.objects.filter(approved=True)
    # list_posts = Post.objects.all()

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts
    }

    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name=name,
        email=email,
        message=message)

    return render(request, 'contact_succes.html', {'name': name, 'email': email, 'message': message})
