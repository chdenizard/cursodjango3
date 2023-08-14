from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post, Contact, ProdutividadeBase, ProdutividadeAdt, ProdutividadeSedoc

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'approved']
    search_fields = ['title','sub_title']
    
    def get_queryset(self, request):
        return Post.objects.all()
    
class ProdutividadeBaseAdmin(admin.ModelAdmin):
    list_display = ['name','secao','percentual']

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(ProdutividadeSedoc)
admin.site.register(ProdutividadeBase, ProdutividadeBaseAdmin)
admin.site.register(ProdutividadeAdt)