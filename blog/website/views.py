from django.shortcuts import render
from django.http import HttpResponse


def hello_blog(request):
    lista = ['Django','Python']
    data = {'name': 'Curso de Django 3', 'lista_tecnologia': lista}
    return render(request, 'index.html', data)