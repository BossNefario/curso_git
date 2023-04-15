class Carro:
    def __init__(self, placa, cor, modelo):
        self.placa = placa
        self.cor = cor
        self.modelo = modelo

    def __str__(self):
        return f"Carro modelo {self.modelo} da cor {self.cor} com placa {self.placa}"

var_carro = Carro('abc-1234', 'vermelho', 'Fusca')
print(var_carro)