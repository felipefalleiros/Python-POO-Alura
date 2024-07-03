# Indica que a classe é abstrata
from abc import ABC, abstractmethod

# A classe está herdando de ABC
class ItemCardapio(ABC):
    def __init__(self,nome, preco) -> None:
        self._nome = nome
        self._preco = preco

    # Método abstrato apenas serve de modelo para as classes derivadas
    @abstractmethod
    def aplicar_desconto(self):
        pass
