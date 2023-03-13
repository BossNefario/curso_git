def fatorial(numero):
    print("Chamada com Parametro", numero)
    if numero == 1:
        return 1
    return numero * fatorial (numero - 1)
n = int(input("Digite um número:"))
retorno = fatorial(n)

print(retorno)