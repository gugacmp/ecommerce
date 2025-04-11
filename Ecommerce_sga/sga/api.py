from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pedido, Transportadora
import requests

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
        return Response({"erro": "Pedido não encontrado"}, status=404)


def gerar_etiqueta(pedido):
    r = requests.post(pedido.transportadora.api_url + "/gerar_etiqueta", json={
        "pedido_id": pedido.id,
        "destinatario": pedido.cliente.endereco,
    }, headers={"Authorization": f"Bearer {pedido.transportadora.token_api}"})
    return r.json().get("etiqueta_url")

@app.task # type: ignore
def atualizar_status_pedidos():
    for pedido in Pedido.objects.exclude(codigo_rastreamento=None):
        status = consultar_api_rastreamento(pedido) # type: ignore
        pedido.status = status
        pedido.save()
