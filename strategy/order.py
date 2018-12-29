#!/usr/bin/python3

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # o Contexto

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:2f} due: {:2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): # a Estratégia: uma classe-base abstrata

    @abstractmethod
    def discount(self, order):
        """Delvolve o desconto como um valor positivo em dólares"""

class FidelityPromo(Promotion): # a primeira Estratégia Concreta
    """5% de desconto para clientes com mil ou mais pontos no programa de fidelidade"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromotion(Promotion): # segunda estratégia concreta
    """10% de desconto para cada LineItem com 20 ou mais unidades"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    """7% de desconto para pedidos com 10 ou mais itens diferentes"""

    def discount(self, order):
        distinct_itens = {item.product for item in order.cart}
        if len(distinct_itens) >= 10:
            return order.total() * .07
        return 0
