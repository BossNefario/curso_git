def gorjeta(valor, porcentagem):
    resultado = valor_conta * porcentagem / 100
    return resultado
valor_conta = float(input())
porcentagem = int(input())
resultado = gorjeta(valor_conta, porcentagem)
print(f"{resultado:.2f}")