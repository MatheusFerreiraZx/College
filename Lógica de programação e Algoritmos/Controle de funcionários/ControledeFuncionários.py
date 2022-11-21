#Apresentação
print("Seja bem vindo ao App de Controle de Funcionários do Matheus Ferreira da Silva Nascimento,\n "
"Registro Uninter: 4282406")

#Variáveis
menu_da_mercearia = {
    1: 'Cadastrar Produto',
    2: ['Consultar Produto', {
        1: 'Consultar Todos os Produtos',
        2: 'Consultar Produto por Código',
        3: 'Consultar Produto(s) por Fabricante',
        4: 'Retornar',
    }],
    3: 'Remover Produto',
    4: 'Sair'
}

def FUN_menu(menu: dict) -> None:  #Função que imprime as opções dos menus

    for key, val in menu.items():
        print(f"{key} - {val if type(val) == str else val[0]}")

    print('-' * 30)

def mostrar_menu(menu: dict) -> int:  #Função que imprime e valida a opção do menu

    print(f"\n{'Menu Principal':-^30s}")
    FUN_menu(menu)

    while True:
        try:
            opcao = int(input("Escolha a opção desejada: "))

            #Verifica se a opção está presente no dicionário do menu
            #Se sim, limpa a tela e retorna a opção selecionada
            if opcao in menu.keys():
                break
            else:
                print("\nOpção inválida!\n")

        except ValueError:
            print("\nOpção inválida.\n")

    return opcao

def cadastrarProduto(codigo: int) -> None:  #Função que cadastra produtos

    print("\nOpção Cadastrar Produto\n")

    print("Código da Produto {:>03}".format(codigo))

    nome = input("Digite o nome do produto: ").strip()
    fabricante = input("Digite o fabricante do produto: ").strip()

    while True:
        try:
            valor = float(input("Digite o valor (R$) do produto: "))

            #Verifica se o valor é maior que zero
            if valor <= 0:
                print("\nALERTA!!!! Digite um valor maior que zero.\n")
            else:
                break

        except ValueError:
            print("\nALERTA!!! Digite um número válido.\n")

    produtos[codigo] = []
    produtos[codigo].append(nome)
    produtos[codigo].append(fabricante)
    produtos[codigo].append(valor)

def removerProduto() -> None:  #Função que remove produtos

    while True:
        try:
            codigo = int(input("\nEscreva o código do produto a ser removido: "))

            #Verifica se existe o produto com o código informado
            #Se sim, remove o produto do dicionário
            if codigo not in produtos.keys():
                print("\nNenhum produto possui esse código.\n")
            else:
                produtos.pop(codigo)

            break
        except ValueError:
            print("\nALERTA!!!! Digite um código válido.\n")

def consultarProduto() -> None:  #Função para consulta de produtos

    #Variável usada para controlar a exibição do menu de consulta
    exibir_menu = True

    cabecalho = f"| {'Código':<10} | {'Nome':<25} | {'Fabricante':<20} | {'Valor (R$)':>10} |"
    len_cabecalho = len(cabecalho)

    while True:

        try:
            #Exibe o menu de consulta
            if exibir_menu:
                print("\nVocê selecionou a opção Consultar Produtos\n")

                print(f"{'Consultar Produtos':-^30s}")
                FUN_menu(menu_da_mercearia[2][1])

            opcao = int(input("Escolha a opção desejada: "))

            #Opção 1 - Consultar Todas os produtos
            if opcao == 1:

                #Lista todas os produtos cadastrados, se houver
                if len(produtos) > 0:
                    print("\nTodos os produtos cadastrados:\n")

                    print("-" * len_cabecalho)
                    print(cabecalho)
                    print("-" * len_cabecalho)

                    for key, val in produtos.items():
                        print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")

                    print("-" * len_cabecalho)
                else:
                    print("\nNão existem produtos cadastradas.")

                print("")

            #Opção 2 - Consultar produto por Código
            elif opcao == 2:
                while True:
                    try:
                        codigo = int(input("\nDigite o código do produto a ser consultado: "))

                        #Exibe o produto com o respectivo código, se houver
                        if codigo in produtos.keys():
                            print("-" * len_cabecalho)
                            print(cabecalho)
                            print("-" * len_cabecalho)

                            print(
                                f"| {codigo:<10} | {produtos[codigo][0]:<25} | {produtos[codigo][1]:<20} | {produtos[codigo][2]:>10.2f} |")

                            print("-" * len_cabecalho)
                        else:
                            print("\nNão existe produto com esse código.\n")

                        print("")

                        break
                    except ValueError:
                        print("\nDigite um código válido.\n")

            #Opção 3 - Consultar produto por Fabricante
            elif opcao == 3:
                while True:
                    try:
                        fabricante = input("\nDigite o fabricante da produto a ser consultada: ")

                        #Variável usada para controlar a exibição do cabeçalho da lista
                        existe_produto = False

                        for key, val in produtos.items():
                            #Imprime os dados do produto do fabricante informado
                            if val[1].upper() == fabricante.upper():
                                if not existe_produto:
                                    print("-" * len_cabecalho)
                                    print(cabecalho)
                                    print("-" * len_cabecalho)

                                print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")

                                existe_produto = True

                        if not existe_produto:
                            print("\nNão existe produto com esse fabricante.\n")
                        else:
                            print("-" * len_cabecalho)

                        break
                    except ValueError:
                        print("Digite um fabricante válido.")

            elif opcao == 4:
                break
            else:
                print("\nAtenção! Você digitou uma opção inválida.\n")

            exibir_menu = True

        except ValueError:
            print("\nAtenção! Você digitou uma opção inválida.\n")
            exibir_menu = False

produtos = {}

while True:
    opcao_selecionada = mostrar_menu(menu_da_mercearia)

    if opcao_selecionada == 1:
        cod_produtos = len(produtos) + 1
        cadastrarProduto(cod_produtos)

    elif opcao_selecionada == 2:
        consultarProduto()

    elif opcao_selecionada == 3:
        removerProduto()

    else:
        break