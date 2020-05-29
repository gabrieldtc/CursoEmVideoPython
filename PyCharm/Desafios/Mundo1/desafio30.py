# crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
num = int(input('Digite um numero qualquer: '))

if (num % 2) == 0:
    print('O numero digitado {} é par!!!'.format(num))
else:
    print('O numero digitado {} é impar!!!'.format(num))