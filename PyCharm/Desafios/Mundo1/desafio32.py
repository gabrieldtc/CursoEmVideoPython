# faça um ´rograma que leia um ano qualquer e diga se ele é bixesto
from datetime import date

ano =  int(input('Digite um ano, ou coloque 0(Zero) para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year
bi = ano % 4

if bi == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é bixexto'.format(ano))
else:
    print('O ano {} nao é bixesto'.format(ano))