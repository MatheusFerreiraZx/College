preco = float(input('digite o preço do produto aqui:'))
p = float(input('digite aqui o percentual de desconto desejado (0-100)%:'))

desconto = preco * (p / 100 )
final = preco - desconto

print('o preço do produto é {}, desconto de {}%'.format(preco, desconto))
print('o Valor do calculado do desconto: {}. O Valor final do produto: {}'. format(desconto, final))