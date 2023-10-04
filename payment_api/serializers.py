from rest_framework import serializers
from .models import Conta, Pagamento

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['numero', 'nome', 'saldo']


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'