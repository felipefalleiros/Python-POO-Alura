# Nome da classe
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    
    restaurantes = []

    # Construtor, sempre que criar a instância de um objeto, ele será chamado
    def __init__(self, nome, categoria):
        
        # Atributos da classe
        self._nome = nome.title() 
        self._categoria = categoria
        # Atributo protegido, que só deve ser acessado dentro da classe. Por convenção se utiliza _ (underline)antes do nome
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        # Todo restaurante criado será colocado na lista restaurantes
        Restaurante.restaurantes.append(self)
        
    # retorna uma representação de string do objeto e não seu local na memória
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # Criando meu próprio método para classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    # decorador que modifica como o atributo vai ser lido
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    # Método de instância, quando chamado precisa ser referenciado por uma instância da classe
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliaca(self, cliente, nota):
        if 0 < nota <= 5:
            # Utiliza a classe Avalicao criada no arquivo avaliacao.py
            avaliacao = Avaliacao(cliente, nota)
            # Adiciona a avaliacao na lista de avaliacoes criada como atributo da classe restaurante
            self._avaliacao.append(avaliacao) 

    @property
    def media_avaliacoes(self):
        # Caso não tenha nenhuma nota na lista
        if not self._avaliacao:
            return '-'
        
        # Soma apenas as notas do objeto avaliacao criado em receber_avaliacao
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        # Arredonda covalor com 1 casa decimal
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        # adiciona a lista apenas se o item for uma instancia da classe ItemCardapio
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restauramte {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            # Verifica se o item tem o atributo descricao, para diferenciar prato de bebida
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)