print('\033[1;31;43mOlá Mundo!\033[m')
print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[7;30mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m!!!'.format(a,b))

nome = 'Gabriel'
print('Prazer em te connhecer {}{}{}'.format('\033[4;33m', nome, '\033[m'))

res = 5 * 3 ** 2

print(res)

nome = 'Joao dos Anjos Moura'
print(nome[1:10:2].upper())

n1 = '7'

n2 = 4

print(n1 + str(n2))

num = '7'
res = int(num) / 2
print(type(res))

from random import randint
num = randint(1, 6)
res = num // 2
print(res)

frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())

texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)