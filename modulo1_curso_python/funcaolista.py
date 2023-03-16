def cadastro():
    while entradas >= 1:
        minha_lista = []
        minha_lista.append(input("Inserir dados da lista: "))
        entradas -= 1
    print(minha_lista)
entradas = int(input("Quantos dados você quer inserir: "))
print(cadastro())   
