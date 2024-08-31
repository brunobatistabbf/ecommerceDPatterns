from decorator.interface import Produto

class Proxy(Produto):
    def __init__(self, produto: Produto):
        self._produto = produto
        self._acesso = True

    def acesso(self, permitido: bool) -> object:
        self._acesso = permitido

    def descricao(self) -> str:
        if self._acesso:
            return  self._produto.descricao()
        else:
            return "SEM ACESSO!!!"