from random import choice
# um professor quer sortear  um dos seu quatro alunos para apagaro quadro. Faça um programa que ajude ele,
# lendoo nome deles e escrevendo o nome escolhido

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digiteo quarto nome: '))
lista = [nome1, nome2, nome3,nome4]
escolhido = choice(lista)
print('o aluno escolhodo foi {}'.format(escolhido))