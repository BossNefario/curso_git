def primeiro_decorator(func):

    def primeira_func():
        print("Execução antes da Função")

        func()

        print("Execução depois da Função")

    return primeira_func

@primeiro_decorator
def funcao_utilizadora():
    print("Preciso utilizar o decorator")

funcao_utilizadora()