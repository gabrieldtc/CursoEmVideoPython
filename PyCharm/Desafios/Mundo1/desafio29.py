# escreva um programa que leia a velocidade de um carro se ultrapassar de 80Km/h mostar uma mensagem dizendo
# que ele foi multado a multa vai custar R$ 7,00 a cada quilimetro ultrapassado

velo = int(input('Qual a velocidade que você passou no radar? '))
multa = 0
if velo > 80:
   multa = float(velo - 80) * 7
   print('Você passou a 80km/h e o valor da multa é R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')