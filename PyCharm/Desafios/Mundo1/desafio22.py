# crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - o nome com todas as letras maisculas
# 2 - o nome com todas as letras minusculas
# 3 - quantas letras sem considerar os espaços
# 4 - quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('seu nome em letras minusculas é {}'.format(nome.lower()))
print('o seu nome ao todo tem {} letras'.format(len(nome) -  nome.count(' ')))
nome1 =nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))
