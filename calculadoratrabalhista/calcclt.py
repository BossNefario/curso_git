salario = float(input("Digite seu sálario bruto(obs: use '.' - ponto - para separar as casas decimais): R$ "))
dicionarioinss = {'faixa1' : 0.075, 'faixa2' : 0.09, 'faixa3' : 0.12, 'faixa4' : 0.14 , 'teto' : 887.27}
dicionariodeducoesinss = {'faixa1' : 0, 'faixa2' : 19.53, 'faixa3' : 96.67, 'faixa4' : 173.80}
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
salario_e_recolhidos = salario_liquido + recolhido_pela_empresa
print(f'Seu sálario líquido considerando os descontos relacionados aos impostos é de: R$ {salario_liquido:.2f}')
print(f'Valor Total considerando sálario líquido e demais valores recolhidos pela empresa é de: R$ {salario_e_recolhidos:.2f}')
print(f'Recebendo como PJ, você terá que recolher Imposto de Renda e INSS (claro se quiser se aposentar ou ainda não for aposentado)')
print(f'Além disso, não ocorrem os recolhimentos de férias, Décimo Terceiro e FGTS')


# pra definir se o modelo de PJ é vantajoso ou não para o profissional precisamos fazer uma avaliacao
# sobre o salario liquido mais os recebidos. Para isso vou construir uma tabela que use os valores obtidos
# de salario liquido frente aos valores de referencia na tabela do INSS e IRRF simultaneamente.
# valores de referência de salario liquido [1204.35, 1752.14, 2228.96, 2514.7, 3189.74, 3260.36, 3772.0, 5320.09]
# utilizei a calculadora auxiliar pra definir esses valores. 17/03/2023

if salario_e_recolhidos < 1204.35:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa1']) - dicionariodeducoesinss['faixa1']
    salario_bruto_irrf = salario_e_recolhidos
elif salario_e_recolhidos <= 1752.14:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa2']) - dicionariodeducoesinss['faixa2']
    salario_bruto_irrf = salario_e_recolhidos
elif salario_e_recolhidos <= 2228.96:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa2']) - dicionariodeducoesinss['faixa2']
    salario_bruto_irrf = salario_e_recolhidos / (1 - dicionarioirrf['faixa1']) - dicionariodeducoesirrf['faixa1']
elif salario_e_recolhidos <= 2514.70:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa3']) - dicionariodeducoesinss['faixa3']
    salario_bruto_irrf = salario_e_recolhidos / (1 - dicionarioirrf['faixa1']) - dicionariodeducoesirrf['faixa1']
elif salario_e_recolhidos <= 3189.74:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa3']) - dicionariodeducoesinss['faixa3']
    salario_bruto_irrf = salario_e_recolhidos / (1 - dicionarioirrf['faixa2']) - dicionariodeducoesirrf['faixa2']
elif salario_e_recolhidos <= 3260.36:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa3']) - dicionariodeducoesinss['faixa3']
    salario_bruto_irrf = salario_e_recolhidos / (1 - dicionarioirrf['faixa3']) - dicionariodeducoesirrf['faixa3']
elif salario_e_recolhidos <= 3772.00:
    salario_bruto_inss = salario_e_recolhidos / (1 - dicionarioinss['faixa4']) - dicionariodeducoesinss['faixa4']
    salario_bruto_irrf = salario_e_recolhidos / (1 - dicionarioirrf['faixa3']) - dicionariodeducoesirrf['faixa3']
elif salario_e_recolhidos <= 5320.09:
    salario_bruto_inss = (salario_e_recolhidos - dicionariodeducoesinss['faixa4']) * (1 - dicionarioinss['faixa4']) 
    salario_bruto_irrf = (salario_e_recolhidos - dicionariodeducoesirrf['faixa4']) * (1 - dicionarioirrf['faixa4']) 
else:
    salario_bruto_inss = dicionarioinss['teto']
    salario_bruto_irrf = salario_e_recolhidos * (1 - dicionarioirrf['faixa4']) - dicionariodeducoesirrf['faixa4']
salario_bruto = salario_e_recolhidos + salario_bruto_inss + salario_bruto_irrf
print(f'O salário bruto para PJ onde o valor seria igual ao da CLT seria: R$ {salario_bruto:.2f}.')