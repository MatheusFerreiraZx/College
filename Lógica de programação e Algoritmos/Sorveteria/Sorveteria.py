#Apresentação
print("Seja bem vindo ao App de Sorveteria do Matheus Ferreira da Silva Nascimento")

print("----------------------------------Carpádio---------------------------------------------------")
print("Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |")
print(" TR    | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |     R$ 18,00       |")
print(" ES    | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |     R$ 21,00       |")
print(" PR    | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |     R$ 24,00       |")
print("---------------------------------------------------------------------------------------------")

#Variáveis
Tamanho = ["P", "M", "G"]

Codigos = {"TR": [6.00, 10.00, 18.00],

           "ES": [7.00, 12.00, 21.00],

           "PR": [8.00, 14.00, 21.00]}

Compra = []

#Condição
while True:

    qual_tamanho = input("Qual o tamanho do sorvete desejado? ")

    qual_sabor = input("Qual o código do sorvete desejado? ")

    if qual_tamanho in Tamanho and qual_sabor in Codigos:

        pedido = Codigos[qual_sabor][Tamanho.index(qual_tamanho)]
        Compra.append(pedido)
        algo_mais = input("Deseja pedir algo mais?"

                          "\nDigite S para sim ou N para não. ")

        if algo_mais == "S":
            continue
        else:
            break
    else:
        print("TAMANHO ou CÓDIGO inválido(s)")
        continue

print("Valor total da compra:", "R$", sum(Compra))
