#crie um proframa que leia quanto em dineiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#US$ 1,00 = R$ 3,27

dinheiro = float(input('Digite quanto de dinheiro você tem? R$ '))

dolar = dinheiro / 3.27
euro = dinheiro / 4.74
iene = dinheiro / 0.039
guarani = dinheiro / 0.00067
print('O valor de R$ {} reais, voce pode comprar ate:\n USS$ {:.2f} dolares \n EUR$ {:.2f} euros \n JPY$ {:.2f} ienes \n PGY$ {:.2f} guaranis'.format(dinheiro,dolar, euro, iene, guarani))