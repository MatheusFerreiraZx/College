
def  metragem_limpeza():
    valor = 0  # Inicialização da variável
    while True:  # Início do laço de repetição
        try:  # Incio do tratamento de erro em dados de entrada
            metragemf = float(input('Digite a área (em m²):\n'
                                    '-->  '))
            if 30 <= metragemf < 300:  # Desvio condicional realizado para verificar o tamanho da área.
                valor = 60 + (0.3 * metragemf)
                print('É necessário contratar 1 pessoa')
                return valor
            elif 300 <= metragemf < 700:
                valor = 120 + (0.5 * metragemf)
                print('É necessário contratar 2 pessoas')
                return valor
            elif metragemf >= 700:
                print('Área igual ou superior à 700 m² não são aceitas.')
                continue
            else:
                print('Área menor que 30 m² não são aceitas.')
                continue
        except ValueError:  # Tratamento de erro caso o usuário entre com caracteres não permitidos.
            print('Erro de entrada. Apenas números são aceitos.')
            continue

# ------------------------------- Fim função valor_metragem ----------------------

# ------------------------------- Início função tipo_limpeza ---------------------

def tipo_limpeza():
    while True:  # Início do laço de repetição
        tipol = input('Digite o tipo de limpeza a ser realizada:\n''B - Básica\n''C - Completa\n''-->  ')
        if tipol.lower() == 'b':  # Desvio condicional para verificar o tipo de limpeza. Foi utilizado o método lower().
            return 1.0
        elif tipol.lower() == 'c':
            return 1.3
        else:
            print('Tipo de limpeza não encontrada. Tente novamente.')
            continue
# ------------------------------- Fim função tipo_limpeza ------------------------

# ------------------------------- Início função adicional ------------------------

def adicional_limpeza():
    valor = 0
    while True:  # Estrutura de repetição para loop infinito.
        try:  # Inicio do tratamento de erro em dados de entrada
            op = int(input('Deseja mais alguma coisa? Veja os adicionais:\n'
                           '0 - Sair\n'
                           '1 - Passar 10 peças de roupa - R$ 10.00\n'
                           '2 - Limpar 1 forno ou micro-ondas - R$ 12.00\n'
                           '3 - Limpar 1 geladeira ou freezer - R$ 20.00\n'
                           '-->  '))
            if op == 0:
                break
            elif op == 1:
                valor += 10
            elif op == 2:
                valor += 12
            elif op == 3:
                valor += 20
            elif op != (0 or 1 or 2 or 3):
                print('Valor não permitido. Tente novamente\n')
                pass
            adicionar_outro = input('Deseja continuar adicionando outro serviço (s/n)?\n')
            if adicionar_outro.lower() == 's':
                continue
            elif adicionar_outro.lower() == 'n':
                break
            else:
                print('Digite apenas sim(s) ou não(n).Tente Novamente...\n')
                continue


        except ValueError:  # Tratamento de erro caso o usuário entre com caracteres não permitidos.
            print('Erro de entrada. Digite um valor valido.\n')
    return valor


# ------------------------------- Fim função adicional ---------------------------

# ------------------------------    INÍCIO DA MAIN   -------------------------------

print("Seja bem vindo ao App de Serviço de Limpeza do Matheus Ferreira da Silva Nascimento")

metragem = metragem_limpeza()  # Atribuição do retorno da função na variável metragem
print(f'R$ {metragem:5.2f}')
tipo = tipo_limpeza()  # Atribuição do retorno da função na variável tipo
print(tipo)
adicionais = adicional_limpeza()  # Atribuição do retorno da função na variável adicionais
print(f'R$ {adicionais:5.2f}')
valorTotal = metragem * tipo + adicionais  # Atribuição do retorno da função na variável valorTotal
print(f'Composição de preços:\n'  # Saída com resumo de serviços/adicionais contratados.
      f'------------------------------------------\n'
      f'Metragem: R${metragem:5.2f}\n'
      f'Tipo de limpeza: {tipo}\n'
      f'Adicional: R${adicionais:5.2f}\n'
      f'-----------------------------------------\n')
print(f'TOTAL: R$ {valorTotal:5.2f}')

# ------------------------------     FIM DA MAIN   ---------------------------------
