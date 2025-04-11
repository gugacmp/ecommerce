from django import forms # type: ignore
from .models import Produto, Venda
from .models import Marketplace

"""
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'foto', 'preco', 'tamanho', 'cor', 'quantidade', 'estoque']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'ativo': forms.CheckboxInput(),
            'destaque': forms.CheckboxInput(),
        }
"""
class ProdutoForm(forms.Form):
    codigo = forms.CharField(label="Código do Produto", max_length=100, required=True)
    sku = forms.CharField(label="SKU", max_length=100, required=False)
    nome = forms.CharField(label="Nome do Produto", max_length=255, required=True)
    marca = forms.CharField(label="Marca", max_length=100, required=False)
    categoria = forms.CharField(label="Categoria", max_length=100, required=False)
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea, required=False)
    foto = forms.ImageField(label="Foto do Produto", required=False)

    preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2, required=True)
    preco_promocional = forms.DecimalField(label="Preço Promocional", max_digits=10, decimal_places=2, required=False)

    peso = forms.DecimalField(label="Peso (kg)", max_digits=6, decimal_places=2, required=False)
    altura = forms.DecimalField(label="Altura (cm)", max_digits=6, decimal_places=1, required=False)
    largura = forms.DecimalField(label="Largura (cm)", max_digits=6, decimal_places=1, required=False)
    comprimento = forms.DecimalField(label="Comprimento (cm)", max_digits=6, decimal_places=1, required=False)

    tamanho = forms.CharField(label="Tamanho", max_length=50, required=False)
    cor = forms.CharField(label="Cor", max_length=50, required=False)

    quantidade = forms.IntegerField(label="Quantidade", required=True)
    estoque = forms.IntegerField(label="Estoque", required=True)

    ativo = forms.BooleanField(label="Produto Ativo", required=False, initial=True)
    destaque = forms.BooleanField(label="Destacar na Home", required=False)


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['codigo_produto', 'quantidade', 'status']


class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = ['nome', 'status', 'token']
