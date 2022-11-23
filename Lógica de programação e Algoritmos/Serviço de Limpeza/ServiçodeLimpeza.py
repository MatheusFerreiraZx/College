#Apresentação
print("Seja bem vindo ao App de Serviço de Limpeza do Matheus Ferreira da Silva Nascimento\n")

#Função metragem da limpeza
def metragem_limpeza():
    metragem = input("Qual a metragem da porção a ser limpa? ")

    try:
        metragem = int(metragem)
        if not 30 <= metragem < 700:
            metragem_limpeza()

        else:
            metragem = int(metragem)
            if 30 <= metragem < 300:
                valor_metragem = 60 + 0.3 * metragem
            else:
                valor_metragem = 120 + 0.5 * metragem
            return valor_metragem

    except:
        metragem_limpeza()

#Função tipo de limpeza
def tipo_limpeza():
    tipo = input("Qual o tipo de limpeza será feita? Digite B para básica e C para completa. ")
    if tipo == "B":
        multiplicador = 1.00
    elif tipo == "C":
        multiplicador = 1.30
    else:
        tipo_limpeza()
    return multiplicador


#Função adicional da limpeza
def adicional_limpeza():
    aux = 0
    print(Tipos_adicionais)

    while True:

        adicional = input("Digite o número do adicional que deseja. ")
        if int(adicional) == 0:
            break
        elif int(adicional) in Tipos_adicionais:
            aux = aux + Valor_adicional[int(adicional)]
        else:
            continue
    return aux


#tabela adicionais

Tipos_adicionais = {0: "Sem adicionais",

                   1: "Passar 10 peças de roupa",

                   2: "Limpeza de Forno/Microondas",

                   3: "Limpeza de Freezer/Geladeira"}

Valor_adicional = [0, 10.00, 12.00, 20.00]

#Programa
valor = metragem_limpeza()
tipo_limpeza = tipo_limpeza()
adicionais = adicional_limpeza()

total = (valor * tipo_limpeza) + adicionais
print(f"R$ {total:,.2f}")
