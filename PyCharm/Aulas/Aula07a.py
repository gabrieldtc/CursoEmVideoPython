n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
sub = n1-n2
di = n1//n2
e = n1**n2
print('A soma é {},\n o produto é {},\n a divisão é {:.3f} e a subutração é {}'.format(s,m,d,sub), end=' ')
print('Divisão inteira {} e potencia {:.3f}'.format(di,e))
#print('A soma vale {}'.format(n1+n2))