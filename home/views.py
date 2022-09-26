from urllib import response
from .models import Avaliacao, Cliente, Pedido, Produto,Categoria, PedidoItem,Imagens
from .serializer import AvaliacaoSerializer, CategoriaSerializer, ImagemSerializer, PedidoItemSerializer, ProdutoSerializer,PedidoSerializer, ClienteSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from . import views
from home import serializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

class ProdutoList(ListCreateAPIView):
    queryset= Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def post(self, request, *args, **kwargs):
        if float(request.data['preco'])<0:
            return Response({'error':'Preço não pode ser negativo'})
        return super().post(request, *args, **kwargs)
    
class ProdutoDetalhe(RetrieveUpdateDestroyAPIView):
    queryset =  Produto.objects.all()
    serializer_class = ProdutoSerializer
    # lookup_field = 'id'
    
    def delete(self, request, pk):
        produto = get_object_or_404(Produto,pk=pk)
        if produto.qtd_estoque>0:
            return Response({'error':'Produto com quantidade de estoque maior que 0, não poderá ser deletado'})
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self,request,pk, *args, **kwargs):
       produto = get_object_or_404(Produto,pk=pk)
       if float(request.data['preco'])<0 or float(request.data['preco']) > 100 :
        return Response({'error':'Preço não pode ser negativo e nem acima de 100'})
       
       return super().update(request, *args, **kwargs)
 
class ProdutoFiltro(FilterSet):
    class Meta:
        model = Produto
        fields= {
            'categoria_id': ['exact'],
            'qtd_estoque':['gt', 'lt']
        }
   
class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class= ImagemSerializer
   
class ProdutoViewSet(viewsets.ModelViewSet):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
   
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('category_id', 'qtd_estoque')
    filterset_class = ProdutoFiltro    
   
   
    
class AvaliacaoViewSet(viewsets.ModelViewSet):
     queryset = Avaliacao.objects.all()
     serializer_class = AvaliacaoSerializer
     
     def get_queryset(self):
        return Avaliacao.objects.filter(produto_id=self.kwargs['produtos_pk'])
        
class ClienteViewSet(viewsets.ModelViewSet):
     queryset = Cliente.objects.all()
     serializer_class = ClienteSerializer
      
class CategoriaViewSet(viewsets.ModelViewSet):
     queryset= Categoria.objects.all()
     serializer_class = CategoriaSerializer 
     
class PedidoViewSet(viewsets.ModelViewSet):
    queryset= Pedido.objects.all()
    serializer_class = PedidoSerializer 

class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer
    


     
    # def get_queryset(self):
    #     return super().get_queryset()
    
    # def get(self,request):
    #     queryset= Produto.objects.all()
    #     serializer=ProdutoSerializer(queryset,many=True)
    #     return Response(serializer.data)


# @api_view(['GET','POST'])
# def produtos_listar(request):
#     if request.method == 'GET':
#         queryset= Produto.objects.all()
#         serializer=ProdutoSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProdutoSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# @api_view(['GET','PUT','DELETE'])
# def produto_detalhe(request,id):
#         produto = get_object_or_404(Produto,pk=id)
#         if request.method == 'GET':
#             serializer = ProdutoSerializer(produto)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = ProdutoSerializer(produto, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             produto.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET','POST'])
# def pedido(request):
#     if request.method == 'GET':
#         queryset= Pedido.objects.all()
#         serializer=PedidoSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer =PedidoSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','POST'])
# def cliente(request):
#     if request.method == 'GET':
#         queryset= Cliente.objects.all()
#         serializer=ClienteSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer =ClienteSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

