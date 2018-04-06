frase = "Curso em Vídeo Python"

#Fatia a 4 letra da frase
print(frase[3])

#Vai da 4 letra até a 12 letra
print(frase[3:13])

#Do inicio até o 12
print(frase[:13])

#Do 12 até o final
print(frase[13:])

#Da letra 1 até a 14
print(frase[1:15])

#Da letra 1 até a 14, pulando de 2 em 2
print(frase[1:15:2])

#Conta quantas vezes existe determinada coisa
print(frase.count("o"))

#Joga toda a frase em maisculo
print(frase.upper())

#Conta quantas letras tem na frase (COMEÇANDO A CONTAR EM 0) (CONTA ESPAÇAMENTOS)
print(len(frase))

#Remove todos os espaços indesejados na frase
print(frase.strip())

#Troca uma frase por outra
print(frase.replace('Python', 'Android'))

#Verefica se a palavra esta dentro da frase
print("Curso " in frase)

#Joga todas frases em minusculo
print(frase.lower())

#Divide a frase
print(frase.split())

#Encontrando a posição em que a palavra aparece
print(frase.find('a') + 1
