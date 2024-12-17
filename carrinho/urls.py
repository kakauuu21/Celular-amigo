"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import addcarrinho, exibir_carrinho, excluir_carrinho, finalizar_compra, relatorio_compras

urlpatterns = [
    path('addcarrinho/<int:produto_id>/', addcarrinho, name='addcarrinho'),
    path('', exibir_carrinho, name='exibir_carrinho'),
    path('excluir_carrinho/', excluir_carrinho, name='excluir_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('relatorio_compras/', relatorio_compras, name='relatorio_compras'),  # Nova URL
]



