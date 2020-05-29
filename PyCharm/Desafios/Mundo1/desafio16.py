from math import trunc

#crie um programa que leia um mumero Real qualquer pelo teclado e mostre na tela a sua porcao inteira
# EX: diigite o numero 6.127 tem como a parte inteira 6

num = float(input('Digite um numero real: '))
print('O valor digitado é {} e a sua porção inteira é {}'.format(num,trunc(num)))