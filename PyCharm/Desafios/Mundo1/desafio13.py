#faca um algoritmo que leia o salario de um funcionario e mostre o seu novo salario com 15% de almento

#nome = str(input('Digite o seu nome: '))
salario = float(input('Digite o seu salario atual: R$ '))

novoSalario = (salario + (salario * 15) / 100)

print('Seu salario de R$ {:.2f} vai para R$ {:.2f} com almento de 15%'.format(salario, novoSalario))