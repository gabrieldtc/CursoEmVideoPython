# Desenvolva um programa que leia o comprimento de tres retas  e diga ao ususario se elas podem ou nao formar um triangulo
print('-=-'*20)
print('Analizador de triangulo')
print('-=-'*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a seguda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimetos {}, {}, {} podem formar um triangulo.'.format(r1,r2,r3))
else:
    print('Os seguimetos {}, {}, {} nao formam um triangulo.'.format(r1,r2,r3))