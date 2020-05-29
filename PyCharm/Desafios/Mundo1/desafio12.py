# faca um algoritmo que leia um preço e mostre o seu novo preco, com 5% de desconto

#nome = str(input('digite o produto: '))
vlproduto = float(input('Digite o valor do produto: R$ '))
#desc = int(input('Digite o valor do desconto: '))

comdesc = (vlproduto - (vlproduto * 5) / 100)

print('O produto que custava R$ {:.2f} com desconto de 5% fica R$ {:.2f}'.format(vlproduto, comdesc))