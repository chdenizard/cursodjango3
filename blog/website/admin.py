from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'approved']
    search_fields = ['title','sub_title']
    
    def get_queryset(self, request):
        return Post.objects.filter(approved = True)
    

admin.site.register(Post, PostAdmin)