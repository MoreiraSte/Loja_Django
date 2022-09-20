from turtle import update
from django.contrib import admin
from django.db.models import Count, QuerySet,Sum
from . import models
from django.contrib import messages
from django.utils.translation import ngettext



@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display  = ['nome','preco', 'custom_qtd_estoque']
    list_editable =['preco']
    list_filter= ['categoria']
    actions = ['zerar_estoque','aumentar_10','diminuir_10']

    
    def zerar_estoque(self, request, queryset:QuerySet):
        updated = queryset.update(qtd_estoque = 0)
        self.message_user(request, ngettext(
            '%d atualizados/atualizado com sucesso',
            '%d atualizados/atualizado com sucesso',
            updated,
        ) % updated, messages.SUCCESS)
        
    def aumentar_10(self,request,queryset):
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_novo = preco_antigo * 1.10
            produto.preco = preco_novo
            produto.save(update_fields=['preco'])
            #updated = queryset.update(preco = preco_novo)
            
    def diminuir_10(self,request,queryset):
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_novo = preco_antigo * 0.90
            produto.preco = preco_novo
            produto.save(update_fields=['preco'])
      
        
        
    def custom_qtd_estoque(self,produto):
       
        if produto.qtd_estoque == 0 :
            return "Estoque zerado"
        
        elif produto.qtd_estoque < 5 :
            return "Estoque baixo"
       
        if produto.qtd_estoque > 5 :
            return "Estoque alto"
        
@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo']
    search_fields= ['nome__startswith']    

    
admin.site.register(models.Categoria)
admin.site.register(models.Pedido)
admin.site.register(models.PedidoItem)

