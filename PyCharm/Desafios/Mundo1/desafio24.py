# crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com "SANTO"
cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')