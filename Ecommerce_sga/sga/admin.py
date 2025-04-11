from django.contrib import admin
from .models import Produto, Venda

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'estoque')
    search_fields = ('nome',)

class VendaAdmin(admin.ModelAdmin):
    list_display = ('codigo_produto', 'produto', 'quantidade', 'status', 'data_venda', 'valor_total')
    list_filter = ('status',)
    search_fields = ('codigo_produto', 'produto__nome')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
