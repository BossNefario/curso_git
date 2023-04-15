class Fibonacci:

    def __init__(self, maximo):
        self.elemento_atual = 0
        self.prox_elemento = 1
        self.maximo = maximo

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.elemento_atual > self.maximo:
            raise StopIteration
        
        valor_retorno = self.elemento_atual

        self.elemento_atual = self.prox_elemento
        self.prox_elemento = valor_retorno + self.prox_elemento

        return valor_retorno

obj_fibonacci = Fibonacci(10)
print(obj_fibonacci)
for numero in obj_fibonacci:
    print(numero)
print('Final da Iteração')
