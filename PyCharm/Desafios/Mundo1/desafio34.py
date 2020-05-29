# Escreva um programa que pergunte o salario  de um funcionario  e calcule o valor do seu aumento.
# para salarios superiore a R$ 1.250,00 aumento de 10%
# para salarios  inferiores ou iguais 15% de aumento

sal = float(input('Digite o seu salario? R% '))

if sal < 1250:
    nSal = sal + (sal * 15) / 100
else:
    nSal = sal + (sal * 10) / 100
print('Seu salario passou de R${:.2f} para R${:.2f} com o reajuste.'.format(sal,nSal))