from decorator.decorator import Personalizacao
from decorator.interface import Produto

class Cor(Personalizacao):
    def __init__(self, produto: Produto, cor):
        self._produto = produto
        self._cor = cor

    def descricao(self):
        return f"{self._produto.descricao()} com cor {self._cor}"

class Tamanho(Personalizacao):
    def __init__(self, produto: Produto, tamanho):
        self._produto = produto
        self._tamanho = tamanho

    def descricao(self):
        return f"{self._produto.descricao()} com tamanho {self._tamanho}"

class Estampa(Personalizacao):
    def __init__(self, produto: Produto, estampa):
        self._produto = produto
        self._estampa = estampa

    def descricao(self):
        return f"{self._produto.descricao()} com estampa {self._estampa}"