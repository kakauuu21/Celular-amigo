from django.db import models
from produto.models import Produto
from cliente.models import Cliente


class ItemCarrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def total_preco(self):
        return self.quantidade * self.produto.preco

    def _str_(self):
        return f"{self.quantidade} de {self.produto.nome}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f'Pedido {self.id} - {self.cliente.nome}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f'{self.produto.nome} x {self.quantidade}'

    def save(self, *args, **kwargs):
        self.total = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

        self.atualizar_total_pedido()

    def atualizar_total_pedido(self):
        total_pedido = sum(item.total for item in self.pedido.itempedido_set.all())
        self.pedido.total = total_pedido
        self.pedido.save()