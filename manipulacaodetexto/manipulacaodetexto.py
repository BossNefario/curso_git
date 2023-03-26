frase = 'Curso em Video Python'
frase2 = '   aprenda python  '
print(frase[9:21:2]) # da posição 9 até antes da posição 21 de dois em dois
print(frase[:5]) # Do inicio até antes da posição 5
print(frase[9::3])

# Analise de String
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) # incluso fatiamento
print(frase.find('deo')) # encontra o termo buscado retornando a primeira posicao em que ele aparece
print(frase.find('|Android')) # se não encontrado retorna -1
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print(frase.split())
frase3 = frase.split()
print('-'.join(frase3))
