#Apresentação
print("Seja bem vindo ao App de Vendas do Matheus Ferreira da Silva Nascimento,\n "
"Registro Uninter: 4282406")

#Variáveis
ValorProduto = float(input("Digite o valor do produto: "))
QtdProduto = int(input("Digite a quantidade de produtos: "))
Total = ValorProduto * QtdProduto
frete = 0

#Condição
if 0 < QtdProduto <= 11:
    frete = 30.00
elif 11 <= QtdProduto <= 101:
    frete = 60.00
elif 101 <= QtdProduto <= 1001:
    frete = 120.00
elif 1001 <= QtdProduto <= 10001:
    frete = 240.00

#Cálculo do valor total
valor_produto_sem_frete: float= ValorProduto * QtdProduto
valor_produto_com_frete: float= ValorProduto * QtdProduto * frete
print(f'O valor do produto sem frete é R$ {valor_produto_sem_frete:.2f}')
print(f'O valor do produto com frete é R$ {valor_produto_com_frete:.2f}\n'
      f'frete de R$ {frete:.2f}')