from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'sub_title', 'full_name', 'cetegories']
    # barra de pesquisa
    search_fields = ['title', 'sub_title']


# passar a classe para o django donfigurar
admin.site.register(Post, PostAdmin)
