def meu_nome_func():
    var_controle = False
    meu_nome = input("Digite seu nome: ")
    if meu_nome == "Bruno":
        var_controle = True
    print("Olá mundo, meu nome é:",meu_nome)
    return var_controle

#retorno = meu_nome_func()
#if retorno:
    print("Nome válido")
#else:
#    print("Nome inválido")

def soma_dois_numeros(numero1, numero2):
    return numero1 + numero2

def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero
    return soma

resultado_da_soma = soma_dois_numeros(1,2)
print(resultado_da_soma)
soma_varios_num = soma_numeros(1,2,3,4,5)
print(soma_varios_num)