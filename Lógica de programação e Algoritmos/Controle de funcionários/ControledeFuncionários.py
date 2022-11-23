#Apresentação
print("Seja bem vindo ao App de Controle de Funcionários do Matheus Ferreira da Silva Nascimento")

funcionarios_lista = []  #Inicialização de uma lista vazia que ira receber os dicionários na função cadastrar

# ------ |  Início das funções utilizadas nesse programa| ------
def realce_titulo(titulo_exibir):  #Função Realce para destacar um título
    '''
    Essa função serve para dar destaque a uma mensagem.

    :param titulo_exibir: string
    :return:
    '''
    x = str(titulo_exibir)
    tam = int(len(x))
    print('*' * tam)
    print(f'{titulo_exibir}')
    print('*' * tam)


def cadastrar_funcionario(contador):
    '''

    :param contador: int. Serve para alimentar o campo identificação.
    :return: Retorna uma lista com dicionário dos funcionários
    '''
    identificacao = contador
    print()
    print('-=-' * 15)
    nome = input('Digite o nome do funcionário:  ')
    setor = input('Digite o setor do funcionário:  ')
    funcionario = {'identificacao': identificacao,
                   'nome': nome,
                   'setor': setor}  #Estabelece um dicionário com os dados para o cadastro de funcionário
    print('-=-' * 15)
    print()
    funcionarios_lista.append(funcionario.copy())  # Cria uma cópia do dicionário na lista
    return funcionarios_lista


def consultar_todos(colecao):
    '''
    Exibe todos os elementos numa lista com dicionário

    :param colecao: Deve ser uma lista contendo dicionário
    return:
    '''
    for elemento in colecao:  #Laço de repetição para iterar na lista
        print()
        print(' ----- * -----')
        for chave, valor in elemento.items():  #Laço de repetição para iterar no dicionário contido na lista
            print('{}  :  {}\n'.format(chave, valor))
        print(' ----- * -----')


def consultar_por_id(lista_com_dicionarios):
    '''
    Consulta dados por um id dentro de uma lista com dicionário. Exibe na tela os dados do id requerido

    :param lista_com_dicionarios: coleção de lista com dicionários

    :return:
    '''
    op_consultar_id = int(input('Digite o ID do funcionário que deseja buscar:  '))
    for elemento in lista_com_dicionarios:  #Laço de repetição para iterar na lista
        if elemento['identificacao'] == op_consultar_id:  # Desvio condicional para verificação da key dentro do dic
            print()
            print(' --------*-------')
            for i, j in elemento.items():  #Laço de repetição para iterar no dicionário contido na lista
                print('{}  :  {}'.format(i, j))
            print(' --------*-------')
            print()



def consultar_por_setor(lista_com_dicionarios):
    '''
    Consulta dados pelo Setor dentro de uma lista com dicionário. Exibe na tela os dados do setor requerido

    :param lista_com_dicionarios:
    :return:
    '''
    op_consultar_setor = input('Digite o setor deseja buscar:  ')
    for elemento in lista_com_dicionarios:
        if elemento['setor'] == op_consultar_setor:
            print()
            print(' --------*-------')
            for i, j in elemento.items():
                print('{}  :  {}'.format(i, j))
            print(' --------*-------')
            print()
        else:
            print('Setor {} não encontrado'.format(op_consultar_setor))


def remover_funcionario(lista_com_dicionarios):
    '''
    Essa função remove um funcionário cadastrado
    :param lista_com_dicionarios: Colecaçao do tipo lista contendo dicionário como elementos.
    :return:
    '''
    op_remover_funcionario = int(input('Digite o ID do funcionário que deseja remover:  '))
    for elemento in lista_com_dicionarios:
        if elemento['identificacao'] == op_remover_funcionario:
            lista_com_dicionarios.remove(elemento)
        else:
            print('{} não existe'.format(op_remover_funcionario))


# ------ |  Início da Main | ------

contador = 1
while True:
    realce_titulo('CONTROLE DE FUNCIONÁRIOS')
    print()
    try:   #Início Tratamento de excessões.
        opcao = int(input('OPÇÕES:\n'
                          '1 - Cadastrar Funcionário;\n'
                          '2 - Consultar Funcionários\n'
                          '3 - Remover Funcionário\n'
                          '4 - Sair\n'
                          '\n'
                          'Digite a opção que desejar:  '))
        print()
        if opcao == 1:
            realce_titulo('CADASTRAR FUNCIONÁRIO')
            funcionarios_cadastrados = cadastrar_funcionario(contador)
            contador += 1
            print('Cadastro realizado!')
        elif opcao == 2:
            realce_titulo('CONSULTAR FUNCIONÁRIOS')
            opconsultar = int(input('OPÇÕES:\n'
                                    '1 - Consultar TODOS os Funcionários;\n'
                                    '2 - Consultar Funcionários por ID\n'
                                    '3 - Consultar Funcionários por SETOR\n'
                                    '4 - Retornar\n'
                                    '\n'
                                    'Digite a opção que desejar:  '))
            if opconsultar == 1:
                consultar_todos(funcionarios_cadastrados)
                print()
            elif opconsultar == 2:
                consultar_por_id(funcionarios_cadastrados)
                print()
            elif opconsultar == 3:
                consultar_por_setor(funcionarios_cadastrados)
                print()
            elif opconsultar == 4:
                pass
            else:
                print('\n'
                      '\tDigite um valor inteiro dentro do intervalo de 1 à 4.')
                continue   #Retorna ao laço de repetição
        elif opcao == 3:
            remover_funcionario(funcionarios_cadastrados)

        elif opcao == 4:
            print('Encerrando programa...')
            break
    except ValueError:   #Trata a entrada de caracteres
        print('\n'
              '\tErro. Pare de digitar opções que não existem\n')