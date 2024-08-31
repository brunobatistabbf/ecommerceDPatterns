from abc import  ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def descricao(self) -> str:
        pass