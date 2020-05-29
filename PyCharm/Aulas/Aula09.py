frase = '   Curso em Vídeo Python'
print(frase) # frase por completo
print(frase[3]) # mostra o qte tem no terceiro espaco da frase
print(frase[0])
print(frase[3:13]) # vai do 3 ate o 13
print(frase[:13]) # vai do começo ate o 13
print(frase[13:]) # vai do 13 te o final
print(frase[1:15:2]) # vai do 1 ate o 15 pulando de 2 em 2
print(frase[1::2]) # sabe o comeco mas nao sabe o final e vai pulando de 2 em 2
print(frase[::2]) # nao sabe o comeco e nem o final mas vai pulando de 2 em 2
print(frase.count('o')) # contra a qtd de o minusculo
print(frase.upper().count('O')) # ele conta a qtd de O maiusculo
print(len(frase)) # conta a quantidade de caracteres
print(len(frase.strip())) # remove os espaços indesejados
print(frase.replace('Python', 'Android')) # troca python por android
print('Curso' in frase) # se a palavra curso esta dentro de FRASE
print(frase.find('Vídeo')) # aonde começa a palavra
print(frase.lower().find('vídeo')) # transforma a palvra pra minusculo e procura a frase
print(frase.split()) # cria uma lista com as palavras da frase

dividido = frase.split() # atrubui a palavra dividido o que tem na lista de frase
print(dividido[0]) #mostra a primeira palavra da lista
print(dividido[2][3]) # nostra a letra que esta no espaço 3