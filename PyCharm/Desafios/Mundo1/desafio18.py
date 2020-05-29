from math import radians,sin, cos, tan
# faça um programa que leia um angulo qualquer e mostre  na tela o valor so seno,  cosseno, tangente desse amgulo

angulo = float(input('Digite um angulo: '))
print('O seu seno é {:.2f}\n seo cosseno {:.2f} \n sua tangente {:.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))