from urllib import request
from xml.dom.minidom import CharacterData
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator



class hello(models.Model):
    nome=models.CharField(max_length=255, null=True)


# produto, cliente,categoria, endereço

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.categoria

class Produto(models.Model):
    nome=models.CharField(max_length=255)
    desc = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    qtd_estoque = models.IntegerField(validators=[MinValueValidator(0,"O estoque deve ser igual ou superior a 0"), MaxValueValidator(100,"Máximo estoque de 100")])
    
    def __str__(self) -> str:
        return self.nome
    

    
class Cliente(models.Model):
    
    PLANO_BASICO = 'B'
    PLANO_PREMIUM = 'P'
    PLANO_GOD = 'G'
    
    TIPOS_PLANO = [
        (PLANO_BASICO, 'Basico'),
        (PLANO_PREMIUM,'Premium'),
        (PLANO_GOD, 'God')
    ]
    
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.IntegerField( max_length=11)
    data = models.DateField(auto_now_add=True)
    celular = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15, null=True,blank=True) # blank=true - o campo não fica mais obrigatório 
    data_nasc = models.DateField()
    tipo= models.CharField(max_length=1, choices=TIPOS_PLANO,default=PLANO_BASICO)
    
    def __str__(self) -> str:
        return self.nome
    class Meta:
        ordering = ['-nome']
    
class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cidade=models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf=models.CharField(max_length=2)
    numero=models.IntegerField(unique=True, max_length=6)
    complemento = models.TextField()
    cep =  models.IntegerField(max_length=9)
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    
    PAGAMENTO_CONCLUIDO= 'C'
    PAGAMENTO_AGUARDANDO = 'A'
    PAGAMENTO_RECUSADO = 'R'
    
    STATUS_CAMINHO = 'CA'
    STATUS_ENTRGUE = 'EN'
    STATUS_CARRINHO = 'CAR'
    STATUS_PREPARANDO ='PR'
    STATUS_CANCELADO= 'CAN'
    
    FORMA_PIX = 'P'
    FORMA_CARTAO = 'C'
    FORMA_BOLETO = 'B'
    FORMA_DINHEIRO = 'D'
    
    FORMA_PAGAMENTO = [
        (FORMA_PIX, 'Pix'),
        (FORMA_CARTAO, 'Cartao'),
        (FORMA_BOLETO, 'Boleto'),
        (FORMA_DINHEIRO, 'Dinheiro')
    ]
    
    TIPOS_PAGAMENTO = [
        (PAGAMENTO_RECUSADO,'Recusado'),
        (PAGAMENTO_AGUARDANDO, 'Aguardando'),
        (PAGAMENTO_CONCLUIDO,'Concluido')
    ]
    
    STATUS_PEDIDO =[
        (STATUS_CAMINHO, 'A caminho'),
        (STATUS_ENTRGUE,'Entregue ao usuario'),
        (STATUS_PREPARANDO, 'preparando'),
        (STATUS_CARRINHO, 'No carrinho'),
        (  STATUS_CANCELADO, 'pedido cancelado')
    ]
    
    status_pagamento = models.CharField(max_length=1, choices=TIPOS_PAGAMENTO, default=PAGAMENTO_AGUARDANDO)
    status_pedido = models.CharField(max_length=3, choices=STATUS_PEDIDO, default=STATUS_CARRINHO)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_pagamento =  models.CharField(max_length=1, choices=FORMA_PAGAMENTO, default=FORMA_PIX)
    
    def __str__(self) -> str:
        return self.status_pedido
    

class PedidoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    categoria =  models.ForeignKey(Categoria, on_delete=models.PROTECT)
    quantidade = models.PositiveSmallIntegerField()   
    
class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.nota
     