# escreva um programa que pergunte  a quantidade de quilometros percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foia alugado. calcule o preço a pagar sabenco que o carro custa R$ 60,00 o dia
# e R$ 0.15 por km rodado

dias = int(input('Quabtos dias ficou com o carro? '))
km = float(input('Quantos quilometros rodados com o carro? '))

res = dias * 60 + km * 0.15

print('O valor a ser  pago pelos dias é R$ {:.2f}'.format(res))