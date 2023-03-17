salario = float(input("Digite seu sálario bruto(obs: use '.' - ponto - para separar as casas decimais): R$"))

def calculadora_inss():
    dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 992.21}
    dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80 , 'teto' : 877.22}
    if salario > 7087.22:
        inss = dicionarioinss['teto']
    elif salario >= 3641.04:
        inss = salario * dicionarioinss['faixa4'] - dicionariodeducoesinss['faixa4']
    elif salario >= 2427.36:
        inss = salario * dicionarioinss['faixa3'] - dicionariodeducoesinss['faixa3']
    elif salario >= 1302.01:
        inss = salario * dicionarioinss['faixa2'] - dicionariodeducoesinss['faixa2']
    else:
        inss = salario * dicionarioinss['faixa1'] - dicionariodeducoesinss['faixa1']
    return inss
resultado_inss = calculadora_inss()
print(f'O imposto pago para o INSS é de: {resultado_inss:.2f}.')

def calculadora_irrf(): # Imposto de Renda Retido na Fonte
    dicionarioirrf = {'isento' : 0 , 'faixa1' : 0.075 , 'faixa2' : 0.15 , 'faixa3' : 0.225 , 'faixa4' : 0.275}
    dicionariodeducoesirrf = {'isento' : 0 , 'faixa1' : 142.89 , 'faixa2' : 354.80 , 'faixa3' : 636.13 , 'faixa4' : 869.36}
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

def fgts():
    valor_fgts = salario * 0.08
    return valor_fgts
resultado_fgts = fgts()

def decimo_terceiro():
    valor_decimoterceiro = salario / 12
    return valor_decimoterceiro
resultado_decimoterceiro = decimo_terceiro()

def ferias():
    valor_ferias = (salario / 12) * (4 / 3)
    return valor_ferias
resultado_ferias = ferias()
recolhido_pela_empresa = resultado_ferias + resultado_decimoterceiro + resultado_fgts

print(f'O valores a serem recolhidos pela empresa que não estarão incorporados no sálario líquido: R$ {recolhido_pela_empresa:.2f}')
print(f'FGTS -> R$ {resultado_fgts:.2f}')
print(f'Décimo Terceiro -> R$ {resultado_decimoterceiro:.2f}')
print(f'Férias Proporcionais -> R$ {resultado_ferias:.2f}')

salario_liquido = salario - resultado_irrf - resultado_inss
print(f'Seu sálario líquido considerando os descontos relacionados aos impostos é de: R$ {salario_liquido:.2f}')