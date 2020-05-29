nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'GABRIEL':
    print('Que lindo nome você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))