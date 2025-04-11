from django.urls import path
from . import views

urlpatterns = [
    path('configurar_produto/', views.configurar_produto, name='configurar_produto'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/aprovadas/', views.vendas_aprovadas, name='vendas_aprovadas'),
    path('vendas/analise/', views.vendas_analise, name='vendas_analise'),
    path('vendas/canceladas/', views.vendas_canceladas, name='vendas_canceladas'),
    path('processar_pagamentos/', views.processar_pagamentos, name='processar_pagamentos'),
    path('nfe_gerenciamento/', views.nfe_gerenciamento, name='nfe_gerenciamento'),
    path('', views.index, name='index'),  # Página inicial
    path('integrador/', views.integrador_view, name='integrador'),
    path('logistica/', views.logistica, name='logistica'),
    path("api/logistica/frete/", views.calcular_frete, name="calcular_frete"),
    path("api/logistica/status/<str:codigo_pedido>/", views.status_pedido, name="status_pedido"),
]
