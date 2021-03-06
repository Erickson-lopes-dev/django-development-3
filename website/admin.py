from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'cetegories', 'approved', 'id', ]
    # barra de pesquisa
    search_fields = ['title', 'sub_title']

    # exibe apenas os dados com o valor de approved correspondente a True
    # def get_queryset(self, request):
    #     return Post.objects.filter(approved=True)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'email']


# passar a classe para o django configurar
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
