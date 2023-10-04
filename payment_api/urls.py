from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payment_api.views import SaldoView, EnviarPagamentoView, CriarContaView,ContaViewSet

router = DefaultRouter()
router.register(r'contas', ContaViewSet)

urlpatterns = [
    path('saldo/<str:numero>/', SaldoView.as_view(), name='saldo'),
    path('enviar-pagamento/<str:numero>/', EnviarPagamentoView.as_view(), name='enviar_pagamento'),
    path('criar-conta/', CriarContaView.as_view(), name='criar_conta'),  # Rota para criar contas
    path('', include(router.urls)),
]