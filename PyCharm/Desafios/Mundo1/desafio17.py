from math import hypot
# faca um programa que leia o comprimento do cateto ooposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print(' a hipotenusa vai medir {:.2f}'.format(hipotenusa))