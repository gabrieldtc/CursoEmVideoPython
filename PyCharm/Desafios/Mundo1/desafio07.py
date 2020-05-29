#desevolva um programa que leia duas notas de um aluno , calcule e nostre a sua media

nome = str(input('Qual o seu nome: '))
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2)/2

print('O aluno {} teve a media {:.1f}'.format(nome,media))