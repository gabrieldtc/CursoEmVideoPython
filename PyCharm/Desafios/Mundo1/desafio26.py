# crie um programa que leia uma frase pelo teclado e mostre:
# 1 - quantas veses aparece a letra "A"
# 2 -em que posicao ela aparece a primera vez
# 3 - em que posocao ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip()
print('A letra A apareceu {} na frase'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.upper()[0:].find('A')))
print('A ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))

