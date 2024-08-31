from decorator.interface import Produto

class Sistema:
    _instancia = None

    @staticmethod
    def get():
        if Sistema._instancia is None:
            Sistema._instancia = Sistema()
        return  Sistema._instancia

    def comprar(self, produto: Produto):
        print(f"Compra Realizada com Sucesso!!!")
        print(f"{produto.descricao()}")