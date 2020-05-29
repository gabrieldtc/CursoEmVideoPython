#faca um programa que leia a largura  e a altura  de uma parede em metros,
# calcule a sua area
# e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2 metro quadrados

largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))

area = largura * altura

#print(area)

quantidade = area / 2


print('A quantidade de tinta necessaria pintar a parede de {}m2 X {}m2 com a area de {}m2 é {}l de tinta.'.format(largura,altura,area, quantidade))