from django.db import models

class Conta(models.Model):
    numero = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'payment_api_conta'

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    beneficiario = models.CharField(max_length=100)
    remetente = models.CharField(max_length=100)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pagamento de {self.valor} para {self.beneficiario} de {self.remetente}"
