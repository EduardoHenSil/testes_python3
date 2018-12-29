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
            discount = self.promotion(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:2f} due: {:2f}>'
        return fmt.format(self.total(), self.due())


    
def fidelity_promo(order):
    """5% de desconto para clientes com mil ou mais pontos no programa de fidelidade"""

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0
 
def bulk_item_promo(order):
    """10% de desconto para cada LineItem com 20 ou mais unidades"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7% de desconto para pedidos com 10 ou mais itens diferentes"""

    distinct_itens = {item.product for item in order.cart}
    if len(distinct_itens) >= 10:
        return order.total() * .07
    return 0


promos = [globals()[name] for name in globals()
                          if name.endswith('_promo')
                          and name != 'best_promo']
def best_promo(order):
    """Seleciona o melhor deconto disponível"""

    return max(promo(order) for promo in promos)
