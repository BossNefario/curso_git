salario = [1302.00, 1903.97, 2471.30, 2826.26, 3751.05, 3858.94, 4664.68, 7507.50]
dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 992.21}
dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80 , 'teto' : 877.22}
dicionarioirrf = {'isento' : 0 , 'faixa1' : 0.075 , 'faixa2' : 0.15 , 'faixa3' : 0.225 , 'faixa4' : 0.275}
dicionariodeducoesirrf = {'isento' : 0 , 'faixa1' : 142.89 , 'faixa2' : 354.80 , 'faixa3' : 636.13 , 'faixa4' : 869.36}

def calculadora_inss():
    inss_list = []
    for item in salario:
        if item >= 7507.50:
            inss = dicionarioinss['teto']
        elif item >= 3856.94:
            inss = item * dicionarioinss['faixa4'] - dicionariodeducoesinss['faixa4']
        elif item >= 2471.30:
            inss = item * dicionarioinss['faixa3'] - dicionariodeducoesinss['faixa3']
        elif item >= 1302.01:
            inss = item * dicionarioinss['faixa2'] - dicionariodeducoesinss['faixa2']
        else:
            inss = item * dicionarioinss['faixa1'] - dicionariodeducoesinss['faixa1']
        inss_list.append(inss)
    return inss_list
resultado_inss = calculadora_inss()

def calculadora_irrf(): # Imposto de Renda Retido na Fonte
    irrf_list = []
    for item in salario:
        if item < 1903.98:
            irrf = dicionarioirrf['isento']
        elif item <= 2826.66:
            irrf = item * dicionarioirrf['faixa1'] - dicionariodeducoesirrf['faixa1']
        elif item <= 3751.05:
            irrf = item * dicionarioirrf['faixa2'] - dicionariodeducoesirrf['faixa2']
        elif item <= 4664.68:
            irrf = item * dicionarioirrf['faixa3'] - dicionariodeducoesirrf['faixa3']
        else:
            irrf = item * dicionarioirrf['faixa4'] - dicionariodeducoesirrf['faixa4']
        irrf_list.append(irrf)
    return irrf_list

resultado_irrf = calculadora_irrf()

salario_liquido = [s - irrf - inss for s, irrf, inss in zip(salario, resultado_irrf, resultado_inss)]
salario_liquido = [round(valor, 2) for valor in salario_liquido]
print(salario_liquido)

# [1204.35, 1752.14, 2228.96, 2514.7, 3189.74, 3260.36, 3772.0, 5320.09]

