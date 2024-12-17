# Create your views here.
from django.shortcuts import render, redirect
from .models import ItemCarrinho
from produto.models import Produto
from cliente.models import Cliente
from django.contrib import messages
from django.apps import apps
from .models import Pedido
from .models import ItemPedido


def addcarrinho(request, produto_id):
    if request.method == 'POST':
        try:
            produto = Produto.objects.get(id=produto_id)
            quantidade = int(request.POST.get('quantidade', 1))

            cliente_id = request.session.get('cliente_id')
            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)
                ItemCarrinho.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
                messages.success(request, 'Produto adicionado ao carrinho.')
            else:
                messages.error(request, 'Você precisa estar logado para adicionar produtos ao carrinho.')
        except Produto.DoesNotExist:
            messages.error(request, 'Produto não encontrado.')

        return redirect('findex')


def exibir_carrinho(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        itens = ItemCarrinho.objects.filter(cliente_id=cliente_id)
        total = sum(item.total_preco() for item in itens)
        return render(request, 'carrinho.html', {'itens': itens, 'total': total})
    else:
        messages.error(request, 'Você precisa estar logado para ver o carrinho.')
        return render(request, "logincli.html")


def excluir_carrinho(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        ItemCarrinho.objects.filter(cliente_id=cliente_id).delete()
        messages.success(request, 'Carrinho excluído com sucesso.')
    else:
        messages.error(request, 'Você precisa estar logado para excluir o carrinho.')
    return redirect('exibir_carrinho')


def finalizar_compra(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
        itens = ItemCarrinho.objects.filter(cliente_id=cliente_id)

        if itens.exists():
            # Cria o pedido
            total_pedido = sum(item.total_preco() for item in itens)
            pedido = Pedido.objects.create(cliente=cliente, total=total_pedido)

            for item in itens:
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item.produto,
                    quantidade=item.quantidade,
                    preco_unitario=item.produto.preco,
                    total=item.total_preco()
                )

            # Exclui os itens do carrinho após a compra
            itens.delete()

            messages.success(request, 'Compra finalizada com sucesso.')
        else:
            messages.error(request, 'Seu carrinho está vazio.')
    else:
        messages.error(request, 'Você precisa estar logado para finalizar a compra.')

    return redirect('exibir_carrinho')


def relatorio_compras(request):
    Pedido = apps.get_model('carrinho', 'Pedido')
    ItemPedido = apps.get_model('carrinho', 'ItemPedido')

    # Obtém todos os pedidos ou filtra conforme necessário
    pedidos = Pedido.objects.all()

    context = {
        'pedidos': pedidos
    }

    return render(request, 'relatorio_compras.html', context)