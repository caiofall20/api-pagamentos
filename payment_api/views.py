from rest_framework import generics
from .models import Conta, Pagamento
from .serializers import ContaSerializer, PagamentoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView


class SaldoView(generics.RetrieveAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    lookup_field = 'numero'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conta, Pagamento
from .serializers import PagamentoSerializer

class EnviarPagamentoView(APIView):
    def post(self, request, numero):
        # Verifica se a conta especificada na URL existe
        try:
            #import ipdb; ipdb.set_trace()
            conta_remetente = Conta.objects.get(numero=numero)
        except Conta.DoesNotExist:
            return Response({"mensagem": "Conta não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se a conta no JSON corresponde à conta na URL
        if 'numero_conta' in request.data and request.data['numero_conta'] != numero:
            return Response({"mensagem": "Número da conta no JSON não corresponde à URL"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PagamentoSerializer(data=request.data)

        if serializer.is_valid():
            valor_pagamento = serializer.validated_data['valor']

            if conta_remetente.saldo < valor_pagamento:
                return Response({"mensagem": "Saldo insuficiente"}, status=status.HTTP_400_BAD_REQUEST)

            # Adiciona o valor do pagamento ao saldo da conta
            conta_remetente.saldo += valor_pagamento
            conta_remetente.save()

            # Cria o pagamento com o beneficiário definido
            serializer.save(beneficiario=conta_remetente.nome, remetente=conta_remetente.nome, conta=conta_remetente)

            return Response({"mensagem": "Pagamento enviado com sucesso"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        remetente = self.get_object()
        destinatario_numero = request.data.get('destinatario_numero')
        valor = request.data.get('valor')
        destinatario = Conta.objects.filter(numero=destinatario_numero).first()

        if not destinatario:
            return Response({'erro': 'Conta de destinatário não encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        valor = float(valor)
        if remetente.saldo >= valor:
            remetente.saldo -= valor
            destinatario.saldo += valor
            remetente.save()
            destinatario.save()
            return Response({'mensagem': 'Pagamento enviado com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'erro': 'Saldo insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
class CriarContaView(generics.CreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer