def maiusculo(texto):
    return texto.upper()

def minusculo(texto):
    return texto.lower()

def mensagem(funcao):
    texto = funcao("Bruno Almeida")
    print(texto)

mensagem(maiusculo)
mensagem(minusculo)

def somador(x):
    def soma(y):
        return x + y
    
    return soma

resultado = somador(15)

print(resultado(10))

def cumprimento(funcao):
    def saudacao():
        print("Bom Dia !")
        funcao()
        print("Boa Noite !")
    return saudacao

@cumprimento
def boa_tarde():
    print("Boa Tarde !")

boa_tarde()