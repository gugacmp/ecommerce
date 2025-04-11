from django.db import models

"""
class Produto(models.Model):
    TAMANHOS = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]
    
    COR = [
        ('Vermelho', 'Vermelho'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        ('Preto', 'Preto'),
        ('Branco', 'Branco'),
    ]

    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='produtos/')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tamanho = models.CharField(max_length=1, choices=TAMANHOS)
    cor = models.CharField(max_length=20, choices=COR)
    quantidade = models.IntegerField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

    @property
    def valor_total(self):
        return self.preco * self.quantidade
"""
class Produto(models.Model):
    codigo = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    largura = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    comprimento = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    tamanho = models.CharField(max_length=20, blank=True, null=True)
    cor = models.CharField(max_length=30, blank=True, null=True)
    quantidade = models.PositiveIntegerField()
    estoque = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    PENDENTE = 'Pendente'
    APROVADA = 'Aprovada'
    CANCELADA = 'Cancelada'
    EM_ANALISE = 'Em Análise'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (APROVADA, 'Aprovada'),
        (CANCELADA, 'Cancelada'),
        (EM_ANALISE, 'Em Análise'),
    ]

    produto = models.ForeignKey(Produto, related_name='vendas', on_delete=models.CASCADE)
    codigo_produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDENTE)
    data_venda = models.DateTimeField(auto_now_add=True)

    @property
    def valor_total(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f'Venda {self.produto} - {self.codigo_produto} - {self.status}'

from django.db import models

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=20)
    chave = models.CharField(max_length=44)
    cliente = models.CharField(max_length=100)
    data = models.DateField()
    produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('autorizada', 'Autorizada'),
        ('rejeitada', 'Rejeitada'),
        ('cancelada', 'Cancelada'),
        ('denegada', 'Denegada'),
        ('inutilizada', 'Inutilizada')
    ])
    
    def __str__(self):
        return f"NF {self.numero} - {self.cliente}"

from django.db import models

class Marketplace(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    token = models.TextField(blank=True, null=True)

class VendaMarketplace(models.Model):
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    produto = models.CharField(max_length=200)
    data_venda = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

class Transportadora(models.Model):
    nome = models.CharField(max_length=100)
    api_url = models.URLField()
    token_api = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=50, unique=True)
    cliente = models.CharField(max_length=100)
    endereco_entrega = models.TextField()
    status = models.CharField(max_length=50, default='Aguardando envio')
    transportadora = models.ForeignKey(Transportadora, on_delete=models.SET_NULL, null=True)
    codigo_rastreamento = models.CharField(max_length=100, blank=True, null=True)
    etiqueta_url = models.URLField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo_pedido

