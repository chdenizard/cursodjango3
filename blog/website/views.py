from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contact

def hello_blog(request):
    lista = ['Django','Python']
    list_posts = Post.objects.filter(approved=True)
    data = {
        'name': 'Curso de Django 3', 
        'lista_tecnologia': lista, 
        'posts' : list_posts}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

def save_form(request):
    Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message'],
    )
    
    name = request.POST['name']
    
    return render(request, 'contato_recebido.html', {'name_contact': name})