salario = float(input("Digite seu sálario bruto(obs: use '.' - ponto - para separar as casas decimais): R$ "))
dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 877.25}
dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80}
dicionarioirrf = {'isento' : 0 , 'faixa1' : 0.075 , 'faixa2' : 0.15 , 'faixa3' : 0.225 , 'faixa4' : 0.275}
dicionariodeducoesirrf = {'isento' : 0 , 'faixa1' : 142.89 , 'faixa2' : 354.80 , 'faixa3' : 636.13 , 'faixa4' : 869.36}
faixas_irrf = {'isento' : 1903.98, 1 : 2826.66, 2 : 3751.05, 3 : 4664.68}

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
salario_descontado_inss = salario - resultado_inss

def calculadora_irrf_mensal():
    irrf = 0
    if salario_descontado_inss >= faixas_irrf[3]:
        irrf = (salario_descontado_inss - faixas_irrf[3]) * dicionarioirrf['faixa4']
        irrf += (faixas_irrf[3] - faixas_irrf[2]) * dicionarioirrf['faixa3']
        irrf += (faixas_irrf[2] - faixas_irrf[1]) * dicionarioirrf['faixa2']
        irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
    elif salario_descontado_inss >= faixas_irrf[2]:
        irrf += (salario_descontado_inss - faixas_irrf[2]) * dicionarioirrf['faixa3']
        irrf += (faixas_irrf[2] - faixas_irrf[1]) * dicionarioirrf['faixa2']
        irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
    elif salario_descontado_inss >= faixas_irrf[1]:
        irrf += (salario_descontado_inss - faixas_irrf[1]) * dicionarioirrf['faixa2']
        irrf += (faixas_irrf[1] - faixas_irrf['isento']) * dicionarioirrf['faixa1']
    elif salario_descontado_inss >= faixas_irrf['isento']:
        irrf += (salario_descontado_inss - faixas_irrf['isento']) * dicionarioirrf['faixa1']
    else:
        irrf = dicionarioirrf['isento']
    return irrf
resultado_irrf = calculadora_irrf_mensal()
salario_liquido = salario_descontado_inss - resultado_irrf

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

total_com_direitos_trabalhistas = salario_liquido + recolhido_pela_empresa

print(f'Salario: R$ {salario:.2f}')
print(f'INSS: R$ {resultado_inss:.2f}')
print(f'IRRF: R$ {resultado_irrf:.2f}')
print(f'Salario Liquido: R$ {salario_liquido:.2f}')
print(f'FGTS + Férias + 13º Salario: R$ {recolhido_pela_empresa:.2f}')
print(f'Total dos direitos trabalhistas: R$ {total_com_direitos_trabalhistas:.2f}')
'''
from basedereferencia_brutoliquido import *

def buscar_bruto(bruto_liquido, total_com_direitos_trabalhistas):
    for chave in bruto_liquido:
        if bruto_liquido == total_com_direitos_trabalhistas:
            return chave

resultado_pj = buscar_bruto()
print(resultado_pj)
'''