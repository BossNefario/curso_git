def verifica_prefixo(palavra1, palavra2):
    if palavra1 in palavra2:
        return True
    return False

palavra1 = input()
palavra2 = input()
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)