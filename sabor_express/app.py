import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria':'Italiano', 'ativo': False}]


def exibir_nome_do_programa():
    '''Essa função mostra o nome do programa'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Essa função exibe a lista de opções que o usuário pode escolher'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o App'''
    print('Finalizando o app...')

def voltar_ao_menu_principal():
    '''Essa função faz com que o usuário volte para o menu principal do app
    
    Input
    - ENTER para voltar ao menu principal
    '''
    input('\nAperte ENTER para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    '''Essa função mostra o subtitulo de cada opção do menu, quando eles são executados'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Essa função informa ao usuário que ele escolheu uma opção inválida e retorna ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    # Criando um dicionario com as informações fornecidas
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    # Adicionando o dicionário criado a lista de restaurantes
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função mostra ao usuário todas as informações de cada restaurante cadastrado'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes: 
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # modificando o valor para ativado caso o valore de ativo seja True ou desativado caso o valor de ativo seja False
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Essa função altera o estado do restaurante de ativo para desativado e vice versa
    
    Input
    - Nome do restaurante

    Outputs
    - Alteração de estado do restaurante
    - O restaurante não foi encontrado
    '''
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # alterna o estado do restaurante independente do estado atual ser True ou False
            restaurante['ativo'] = not restaurante['ativo']
            # Utilizando ternary operator
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Função que solicita e a opção desejada pelo usuário
    Input
    - Opção do menu

    Output
    - Executa a opção escolhida
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
        # Else executado caso a opçao escolhida seja um número fora das opçoes definidas
        else:
            opcao_invalida()
    # except executado caso a opção escolhida não seja um número        
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicializa o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()