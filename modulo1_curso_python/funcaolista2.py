executado = False

def cadastro():
    global executado
    
    if executado:
        return
    
    entradas = int(input("Quantos dados você quer inserir: "))
    minha_lista = []
    while entradas >= 1:
        minha_lista.append(input("Inserir dados da lista: "))
        entradas -= 1
    return minha_lista
resultado = cadastro()
print(resultado)