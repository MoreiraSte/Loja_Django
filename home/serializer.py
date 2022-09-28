from decimal import Decimal
from rest_framework import serializers
from  pictures.contrib.rest_framework import PictureField
from home.models import  Avaliacao, Categoria, Cliente, Imagens, PedidoItem, Produto,Pedido

# class ProdutoSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     nome = serializers.CharField(max_length=255)
#     preco = serializers.DecimalField(max_digits=6,decimal_places=2)
#     preco_taxa = serializers.SerializerMethodField(method_name='calculo_taxa')
    
    
#     def calculo_taxa(self,produto:Produto):
#        return produto.preco * DecimalField()

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields = ['id', 'nome','preco','preco_taxa', 'qtd_estoque', 'categoria']
        
    preco_taxa = serializers.SerializerMethodField(method_name='calcular_taxa')
    
    def calcular_taxa(self,produto:Produto):
        return Decimal('%2.f'%(produto.preco*Decimal(1.1)))
    
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id','cliente', 'produto', 'nota']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields = ['id',"cliente",'status_pagamento','status_pedido', 'valor', 'tipo_pagamento']
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields = ['id', 'nome', 'email','cpf','data','celular','telefone','data_nasc','tipo']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']
        
class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = ['id', 'produto','categoria','quantidade']
        
class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Imagens
        fields = ['id','titulo','foto']
    
    foto = PictureField()
    
class AddImgSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Imagens
        fields = ['id','titulo','foto']
    
