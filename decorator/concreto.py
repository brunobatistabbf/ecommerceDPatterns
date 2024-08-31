from decorator.interface import Produto

class ProdutoConcreto(Produto):
    def descricao(self) -> str:
        return "Camisa Básica"
