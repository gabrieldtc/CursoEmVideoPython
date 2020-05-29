#escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

metros = float(input('Digite uma distancia em metros: '))

centimetos = metros * 100
milimetros = metros * 1000
quilometros = metros * 0.001
hectomeros = metros * 0.01
decametros = metros * 0.1
decimetros = metros * 10

print('A medida de {} metros corresponde a :\n {}km \n {}hm \n {:.1f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(metros,quilometros,hectomeros,decametros, decimetros,centimetos, milimetros ))