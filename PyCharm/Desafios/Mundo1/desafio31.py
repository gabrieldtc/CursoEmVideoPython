# desenvolva um programa que pergunte a distancia e, Km
# calcule o preço da passagem cobrando R$ 0.50 com viagens ate 200Km e R$ 0.45 nas viagens mais longas

km = float(input('Qual a distancia percorrida: '))
if km <= 200:
    pas = km * 0.50
else:
    pas = km * 0.45
print('A distancia percorrida é de {}Km, e o valor da passagem é R$ {:.2f}'.format(km,pas))