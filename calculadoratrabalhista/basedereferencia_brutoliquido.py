salario = [round(1200 + i * 0.01, 2) for i in range(0, 1000000001)]
dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 877.25}
dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80}
dicionarioirrf = {'isento' : 0 , 'faixa1' : 0.075 , 'faixa2' : 0.15 , 'faixa3' : 0.225 , 'faixa4' : 0.275}
dicionariodeducoesirrf = {'isento' : 0 , 'faixa1' : 142.89 , 'faixa2' : 354.80 , 'faixa3' : 636.13 , 'faixa4' : 869.36}
faixas_irrf = {'isento' : 1903.98, 1 : 2826.66, 2 : 3751.05, 3 : 4664.68}
salario_descontado_inss = []
salario_liquido = []

def calculadora_inss():
    inss_lista = []
    for item in salario:
        if item > 7507.49:
            inss = dicionarioinss['teto']
        elif item >= 3856.94:
            inss = item * dicionarioinss['faixa4'] - dicionariodeducoesinss['faixa4']
        elif item >= 2471.30:
            inss = item * dicionarioinss['faixa3'] - dicionariodeducoesinss['faixa3']
        elif item >= 1302.01:
            inss = item * dicionarioinss['faixa2'] - dicionariodeducoesinss['faixa2']
        else:
            inss = item * dicionarioinss['faixa1'] - dicionariodeducoesinss['faixa1']
        inss = round(inss, 2)
        inss_lista.append(inss)
    return inss_lista
resultado_inss = calculadora_inss()

for x, y in zip(salario, resultado_inss):
    salario_descontado_inss.append(round(x - y, 2))

def calculadora_irrf_mensal():
    irrf_lista = []
    for item in salario_descontado_inss:
        irrf = 0
        if item >= faixas_irrf[3]:
            irrf = (item - faixas_irrf[3]) * dicionarioirrf['faixa4']
            irrf += (faixas_irrf[3] - faixas_irrf[2]) * dicionarioirrf['faixa3']
            irrf += (faixas_irrf[2] - faixas_irrf[1]) * dicionarioirrf['faixa2']
            irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
        elif item >= faixas_irrf[2]:
            irrf += (item - faixas_irrf[2]) * dicionarioirrf['faixa3']
            irrf += (faixas_irrf[2] - faixas_irrf[1]) * dicionarioirrf['faixa2']
            irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
        elif item >= faixas_irrf[1]:
            irrf += (item - faixas_irrf[1]) * dicionarioirrf['faixa2']
            irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
        elif item >= faixas_irrf['isento']:
            irrf += (item - faixas_irrf['isento']) * dicionarioirrf['faixa1']
        else:
            irrf = dicionarioirrf['isento']
        irrf = round(irrf, 2)
        irrf_lista.append(irrf)        
    return irrf_lista
resultado_irrf = calculadora_irrf_mensal()

for x, y in zip(salario_descontado_inss, resultado_irrf):
    salario_liquido.append(round(x - y, 2))

bruto_liquido = {}
tuplas_salario = list(zip(salario, salario_liquido))
bruto_liquido = dict(tuplas_salario)
