# faça um programa que leia um numero  de 0 ate 9999 e mostre cada video separado
# digite  um numero 1834  unidade:4, dezena:3, centena:8, milhar:1

numero = int(input('Digite um numero de 0 a 9999: '))
#n = str(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analizando o numero {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))