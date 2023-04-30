def mostrar(func):
    def interno():
        print("O usuario atual é : ", end="")
        func()
    return interno

@mostrar
def quem():
    print("Alice")

quem()
