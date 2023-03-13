def conta_letras(letra, frase):
    contagem = 0
    for i in frase:
        if i == letra:
            contagem += 1
    return contagem

letra = input()
frase = input()
saida = conta_letras(letra, frase)
print(saida)