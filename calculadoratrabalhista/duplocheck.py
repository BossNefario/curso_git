salario = 13588.28
dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 992.21}
dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80 , 'teto' : 877.22}
dicionarioirrf = {'isento' : 0 , 'faixa1' : 0.075 , 'faixa2' : 0.15 , 'faixa3' : 0.225 , 'faixa4' : 0.275}
dicionariodeducoesirrf = {'isento' : 0 , 'faixa1' : 142.89 , 'faixa2' : 354.80 , 'faixa3' : 636.13 , 'faixa4' : 869.36}

def calculadora_inss():
    if salario > 7507.49:
        inss = dicionarioinss['teto']
    elif salario >= 3856.94:
        inss = salario * dicionarioinss['faixa4'] - dicionariodeducoesinss['faixa4']
    elif salario >= 2471.30:
        inss = salario * dicionarioinss['faixa3'] - dicionariodeducoesinss['faixa3']
    elif salario >= 1302.01:
        inss = salario * dicionarioinss['faixa2'] - dicionariodeducoesinss['faixa2']
    else:
        inss = salario * dicionarioinss['faixa1'] - dicionariodeducoesinss['faixa1']
    return inss
resultado_inss = calculadora_inss()
print(f'O imposto pago para o INSS é de: R$ {resultado_inss:.2f}.')

def calculadora_irrf(): # Imposto de Renda Retido na Fonte
    if salario < 1903.98:
        irrf = dicionarioirrf['isento']
    elif salario <= 2826.66:
        irrf = salario * dicionarioirrf['faixa1'] - dicionariodeducoesirrf['faixa1']
    elif salario <= 3751.05:
        irrf = salario * dicionarioirrf['faixa2'] - dicionariodeducoesirrf['faixa2']
    elif salario <= 4664.68:
        irrf = salario * dicionarioirrf['faixa3'] - dicionariodeducoesirrf['faixa3']
    else:
        irrf = salario * dicionarioirrf['faixa4'] - dicionariodeducoesirrf['faixa4']
    return irrf
resultado_irrf = calculadora_irrf()
print(f'O imposto de renda retido na fonte é de: {resultado_irrf:.2f}.')

salario_liquido = salario - resultado_inss - resultado_irrf