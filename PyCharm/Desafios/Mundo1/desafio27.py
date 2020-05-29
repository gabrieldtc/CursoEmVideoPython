# faça um progrma que leia um nome completo  de uma pessoa, mostrando em seguida  o primeiro e o ultimo nome separadamentr
nome = str(input('Qual o seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
l = nome.split()
print('Seu primeiro nome {}'.format(l[0]))
print('Seu ultimo nome é {}'.format(l[len(l)-1]))
