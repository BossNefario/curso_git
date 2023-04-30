def ola(func):
    def inner():
        print("Ola ")
        func()
        print("Tudo bem? ")
    return inner

def nome():
    print("Alice")

variavel_func = ola(nome)
variavel_func()