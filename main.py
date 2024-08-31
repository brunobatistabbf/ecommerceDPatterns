from proxy import Proxy
from decorator.concreto import ProdutoConcreto
from decorator.decorators import Cor, Tamanho, Estampa
from singleton import Sistema


def comprar_produto(produto:ProdutoConcreto):

    cores = {
        "Preta",
        "Branca",
        "Cinza"
    }

    tamanhos = {
        "P",
        "M",
        "G",
        "GG"
    }

    estampas = {
        "Florida",
        "Listrada",
        "Xadrez",
        "Lisa"
    }

    cor = input("Qual a cor de escolha?")
    tamanho = input("Qual o tamanho?")
    estampa = input("Qual a estampa?")

    if cor not in cores:
        print("Insira uma Cor Válida")
        return

    if tamanho not in tamanhos:
        print("Insira um Tamanho Válido")
        return

    if estampa not in estampas:
        print("Insira uma Estampa Válida")
        return

    produto_personalizado = Tamanho(produto, tamanho)
    produto_personalizado = Cor(produto_personalizado, cor)
    produto_personalizado = Estampa(produto_personalizado, estampa)

    proxy = Proxy(produto_personalizado)

    sistema = Sistema.get()

    sistema.comprar(proxy)

    proxy.acesso(False) #Bloquea acesso



if __name__ == '__main__':
    produto = ProdutoConcreto()
    print("||-------------------CAMISAS PERSONALIZADAS.COM ------>")
    print()
    print("Personalize sua camisa agora:")
    print("Tamanhos: P, M, G, GG")
    print("Cores: Preta, Branca, Cinza")
    print("Estampa: Florida, Listrada, Xadrez, Lisa")
    print()

    comprar_produto(produto)





