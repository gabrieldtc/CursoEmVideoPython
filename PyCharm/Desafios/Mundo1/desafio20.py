from random import shuffle
# o mesmo professor do ecerciccio anterior quer sortear a ordem  de apresentação dos trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre as ordens sorteadas

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digiteo quarto nome: '))
lista = [nome1, nome2, nome3,nome4]
shuffle (lista)
print('A ordem de apresentação será:')
print(lista)
