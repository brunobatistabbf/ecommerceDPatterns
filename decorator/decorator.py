from decorator.interface import Produto

class Personalizacao(Produto):
    def __init__(self, produto: Produto):
        self._produto = produto

    def descricao(self) -> str:
        return self._produto.descricao()