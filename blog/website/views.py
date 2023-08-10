from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_blog(request):
    lista = ['Django','Python']
    list_posts = Post.objects.all
    data = {
        'name': 'Curso de Django 3', 
        'lista_tecnologia': lista, 
        'posts' : list_posts}
    return render(request, 'index.html', data)