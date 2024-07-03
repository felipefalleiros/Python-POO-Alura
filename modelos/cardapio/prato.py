from modelos.cardapio.item_cardapio import ItemCardapio

# classe prato vai herdar métodos, atributos etc da classe ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao) -> None:
        # super() permite acessar informações de outra classe
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self) -> str:
        return self._nome
    
    def aplicar_desconto(self):
        # aplica um desconto de 5%
        self._preco -= (self._preco * 0.05)