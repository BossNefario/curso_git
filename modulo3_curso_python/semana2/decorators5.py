def logging_soma_ab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " é ", end = "")
        return func(a, b)
    return inner

@logging_soma_ab
def soma_ab(a, b):
    soma = a + b
    print(soma)

if __name__ == "__main__":
    c = int(input())
    d = int(input())
    soma_ab(c ,d)