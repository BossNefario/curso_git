inicio, termino = input().split()
inicio = int(inicio)
termino = int(termino)
dia = 24

if termino > inicio:
    resultado = termino - inicio
elif termino < inicio:
    parcial = dia - inicio
    resultado = parcial + termino
else:
    resultado = dia
print(f"O JOGO DUROU {resultado} HORA(S)")