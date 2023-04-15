from carro import Carro

class Estacionamento:
    def __init__(self, vagas = None):
        self.numero_vagas = vagas
        self.carros = []

    def adiciona_carro(self, carro):
        if self.numero_vagas >= len(self.carros):
            self.carros.append(carro)
        else:
            print("Estacionamento Cheio")

    def procura_carro(self, placa):
        for carro in self.carros:
            if placa == carro.placa:
                return carro

    def __iter__(self):
        return self
    
    def __next__(self):
        raise StopIteration
        return 1

esta = Estacionamento(10)
esta.adiciona_carro(Carro("poi-1234", "azul", "Onix"))
esta.procura_carro("poi-1234")

for carro in esta:
    print(carro)