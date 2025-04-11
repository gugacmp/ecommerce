from django.shortcuts import render, redirect
from .models import Produto, Venda
from .forms import ProdutoForm, VendaForm
from .models import NotaFiscal
from .models import Marketplace, VendaMarketplace
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pedido, Transportadora


import requests

def index(request):
    mais_vendidos = [
    {'nome': 'Camisa Polo', 'vendas': 120},
    {'nome': 'Tênis Esportivo', 'vendas': 95},
    {'nome': 'Relógio Digital', 'vendas': 80},
    {'nome': 'Fone Bluetooth', 'vendas': 76},
    {'nome': 'Calça Jeans', 'vendas': 65},
]

    return render(request, 'sga/index.html', {'ranking': mais_vendidos})
    #return render(request, 'sga/index.html')

# Página de Configuração de Produtos
"""
def configurar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('configurar_produto')
    else:
        form = ProdutoForm()
    return render(request, 'sga/configurar_produto.html', {'form': form})
"""
def configurar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            # Aqui você pode salvar no banco de dados
            # ou processar como quiser
            print(form.cleaned_data)  # Debug
            return redirect('configurar_produto')
    else:
        form = ProdutoForm()

    return render(request, 'sga/configurar_produto.html', {'form': form})



def processar_pagamentos(request):
    return render(request, 'sga/processar_pagamentos.html')

def logistica(request):
    return render(request, 'sga/logistica.html')

""""
def nfe_gerenciamento(request):
    return render(request, 'sga/nfe_gerenciamento.html')
"""
""""
def nfe_gerenciamento(request):
    data = request.GET.get('data')
    numero = request.GET.get('numero')
    chave = request.GET.get('chave')
    cliente = request.GET.get('cliente')

    nfe_list = NotaFiscal.objects.all()

    if data:
        nfe_list = nfe_list.filter(data_emissao=data)
    if numero:
        nfe_list = nfe_list.filter(numero_documento__icontains=numero)
    if chave:
        nfe_list = nfe_list.filter(chave_nfe__icontains=chave)
    if cliente:
        nfe_list = nfe_list.filter(cliente__nome__icontains=cliente)

    context = {"notas": nfe_list}
    return render(request, "sga/nfe_gerenciamento.html", context)
"""

def nfe_gerenciamento(request):
    notas = NotaFiscal.objects.all()
    return render(request, "sga/nfe_gerenciamento.html", {'notas': notas})



# Página de Vendas
def vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'sga/vendas.html', {'vendas': vendas})

# Vendas Aprovadas
def vendas_aprovadas(request):
    vendas = Venda.objects.filter(status=Venda.APROVADA)
    return render(request, 'sga/vendas_aprovadas.html', {'vendas': vendas})

""""
def vendas_aprovadas(request):
    vendas = Venda.objects.filter(status='aprovado')
    total = sum(v.preco * v.quantidade for v in vendas)
    return render(request, 'vendas_aprovadas.html', {
        'vendas': vendas,
        'total': total,
        'quantidade': vendas.count()
    })
"""

# Vendas em Análise
def vendas_analise(request):
    vendas = Venda.objects.filter(status=Venda.EM_ANALISE)
    return render(request, 'sga/vendas_analise.html', {'vendas': vendas})

# Vendas Canceladas
def vendas_canceladas(request):
    vendas = Venda.objects.filter(status=Venda.CANCELADA)
    return render(request, 'sga/vendas_canceladas.html', {'vendas': vendas})

# views.py
from collections import Counter
"""""
def processar_pagamentos(request):
    pagamentos = Pagamento.objects.all() # type: ignore
    status_count = Counter(p.status for p in pagamentos)

    return render(request, 'processar_pagamentos.html', {
        'pagamentos': pagamentos,
        'status_count': {
            'aprovado': status_count.get('aprovado', 0),
            'analise': status_count.get('analise', 0),
            'cancelado': status_count.get('cancelado', 0),
        }
    })

"""


def integrador_view(request):
    marketplaces = Marketplace.objects.all()
    vendas = VendaMarketplace.objects.all()

    total_vendas = {
        'Mercado Livre': vendas.filter(marketplace__nome='Mercado Livre').aggregate(total=models.Sum('valor'))['total'] or 0,
        'Shopee': vendas.filter(marketplace__nome='Shopee').aggregate(total=models.Sum('valor'))['total'] or 0,
        'Amazon': vendas.filter(marketplace__nome='Amazon').aggregate(total=models.Sum('valor'))['total'] or 0,
    }

    context = {
        'marketplaces': marketplaces,
        'total_vendas': total_vendas
    }
    return render(request, 'sga/integrador.html', context)

def obter_vendas_mercado_livre(token):
    url = 'https://api.mercadolibre.com/orders/search?seller=ME&order.status=paid'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['results']
    return []


@api_view(["POST"])
def calcular_frete(request):
    peso = request.data.get("peso")
    cep_destino = request.data.get("cep_destino")
    dimensoes = request.data.get("dimensoes")

    opcoes_frete = []

    for t in Transportadora.objects.filter(ativo=True):
        try:
            res = requests.post(t.api_url + "/frete", json={
                "peso": peso,
                "cep_destino": cep_destino,
                "dimensoes": dimensoes,
                "token": t.token_api
            })
            if res.ok:
                data = res.json()
                data["transportadora"] = t.nome
                opcoes_frete.append(data)
        except Exception as e:
            continue

    return Response(opcoes_frete)


@api_view(["GET"])
def status_pedido(request, codigo_pedido):
    try:
        pedido = Pedido.objects.get(codigo_pedido=codigo_pedido)
        if pedido.codigo_rastreamento:
            url = f"{pedido.transportadora.api_url}/rastreio/{pedido.codigo_rastreamento}"
            headers = {"Authorization": f"Bearer {pedido.transportadora.token_api}"}
            res = requests.get(url, headers=headers)
            if res.ok:
                return Response(res.json())
        return Response({"status": pedido.status})
    except Pedido.DoesNotExist:
        return Response({"erro": "Pedido n\u00e3o encontrado"}, status=404)