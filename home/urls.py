from cgitb import lookup
from django.urls import path, include
from . import views 
from rest_framework_nested import routers

rota = routers.DefaultRouter()
rota.register('produtos', views.ProdutoViewSet, basename='produtos')
# rota.register('avaliacao', views.AvaliacaoViewSet, basename='avaliacao')
rota.register('clientes', views.ClienteViewSet, basename='clientes')
rota.register('categoria', views.CategoriaViewSet, basename='categoria')
rota.register('pedido', views.PedidoViewSet, basename='pedido')
rota.register('pedidoItem', views.PedidoItemViewSet, basename='pedidoItem')
rota.register('avalicoes', views.AvaliacaoViewSet, basename='avaliacoes')
rota.register('imagens', views.ImagemViewSet, basename='imagens')

urlpatterns = rota.urls

