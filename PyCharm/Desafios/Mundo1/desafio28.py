# Escreva um programa que faça o computador "PENSAR" em um numero inteiro de 0 ate 5, para o usuario descobrir,
# qual foi o numrero escolhido pelo computador
# o programa devera dizer se o usuario cenceu ou perdeu

from random import randint
from time import sleep

x = randint(0,5)

print('-=-'*17)
print('Vou pensar em um numero entre 0(zero) e 5(cinco)')
print('-=-'*17)
num = int(input('Em que numero eu pensei: '))
print('Pensando!!!')
sleep(3)
if x == num:
    print('Você venceu!!!')
else:
    print('Voce perdeu!!! Pensei no numero {} e você escolheu {}'.format(x,num))

