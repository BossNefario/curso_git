# Extremelly Basic
'''
a = int(input())
b = int(input())
x = a + b
print("X =", x)
'''

# Area of a Circle
'''
n = 3.14159
r = float(input())
a = n * r ** 2
print(f'A={a:.4f}')
'''

# Simple Sum
'''
a = int(input())
b = int(input())
soma = a + b
print("SOMA =", soma)
'''

# Simple Product
'''
a = int(input())
b = int(input())
prod = a * b
print("PROD =", prod)
'''

# Average 1
'''
a = float(input())
b = float(input())
weight_a = 3.5
weight_b = 7.5
average = ((a * weight_a) + (b * weight_b)) / (weight_a + weight_b)
print(f"MEDIA = {average:.5f}")
'''

# Average 
'''
a = float(input())
b = float(input())
c = float(input())
weight_a = 2
weight_b = 3
weight_c = 5
average = ((a * weight_a) + (b * weight_b) + (c * weight_c)) / (weight_a + weight_b + weight_c)
print(f"MEDIA = {average:.1f}")
'''

# Difference
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
diferenca = (a * b - c * d)
print('DIFERENCA = ', diferenca)
'''

# Salary
'''
employee_number = int(input())
work_hours = float(input())
amount_per_hour = float(input())
payment = work_hours * amount_per_hour
print("NUMBER =", employee_number)
print(f"SALARY = U$ {payment:.2f}")
'''

# Salary with Bonus
'''
seller_name = input()
basis_salary = float(input())
sales_amount = float(input())
bonus_ref = 0.15
payment = basis_salary + sales_amount * bonus_ref
print(f"TOTAL = R$ {payment:.2f}")
'''

# Simple Calculate
'''
code_p1, qty_p1, price_p1 = input().split()
code_p2, qty_p2, price_p2 = input().split()
qty_p1 = int(qty_p1)
qty_p2 = int(qty_p2)
price_p1 = float(price_p1)
price_p2 = float(price_p2)
valor = qty_p1 * price_p1 + qty_p2 * price_p2
print(f'VALOR A PAGAR: R$ {valor:.2f}')
'''
'''
code_p1, qty_p1, price_p1 = map(float, input().split())
code_p2, qty_p2, price_p2 = map(float, input().split())
valor = qty_p1 * price_p1 + qty_p2 * price_p2
print(f'VALOR A PAGAR: R$ {valor:.2f}')
'''

# 1011 - Sphere
'''
raio_esfera = float(input())
pi = 3.14159
volume_da_esfera = (4 / 3) * pi * raio_esfera ** 3
print(f"VOLUME = {volume_da_esfera:.3f}")
'''

# 1012 - Area 
'''
a, b, c = map(float, input().split())
pi = 3.14159
area_triangulo_retangulo_base_a_altura_c = (a * c) / 2
area_circulo_raio_c = pi * c ** 2
area_trapezio_base_ab_altura_c = (a + b) * c / 2
area_quadrado_lado_b = b * b
area_retangulo_a_b = a * b
print(f'TRIANGULO: {area_triangulo_retangulo_base_a_altura_c:.3f}')
print(f'CIRCULO: {area_circulo_raio_c:.3f}')
print(f'TRAPEZIO: {area_trapezio_base_ab_altura_c:.3f}')
print(f'QUADRADO: {area_quadrado_lado_b:.3f}')
print(f'RETANGULO: {area_retangulo_a_b:.3f}')
'''
'''
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
area_triangulo_retangulo_base_a_altura_c = (a * c) / 2
area_circulo_raio_c = pi * c ** 2
area_trapezio_base_ab_altura_c = (a + b) * c / 2
area_quadrado_lado_b = b * b
area_retangulo_a_b = a * b
print(f'TRIANGULO: {area_triangulo_retangulo_base_a_altura_c:.3f}')
print(f'CIRCULO: {area_circulo_raio_c:.3f}')
print(f'TRAPEZIO: {area_trapezio_base_ab_altura_c:.3f}')
print(f'QUADRADO: {area_quadrado_lado_b:.3f}')
print(f'RETANGULO: {area_retangulo_a_b:.3f}')
'''

# 1013 The Greatest
'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maximo = max(a, b, c)
print(maximo, "eh o maior")
'''

# 1014 Consuption
'''
distancia_em_km = int(input())
consumo_em_litros = float(input())
desempenho = distancia_em_km / consumo_em_litros
print(f'{desempenho:.3f} km/l')
'''

# 1015 Distance Between Two Points *error
'''
x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'{distancia:.4f}')
'''

# 1016 Distance
'''
distancia = int(input())
tempo = distancia * 2
print(tempo, "minutos")
'''

# 1017 Fuel Spent
'''
consumo_kml = 12
tempo = int(input())
velocidade_media = int(input())
distancia = velocidade_media * tempo
consumo = distancia / consumo_kml
print(f'{consumo:.3f}')
'''

# 1018 Banknotes
'''
valor = int(input())
notas_100 = valor // 100
valor2 = valor - (notas_100 * 100)
notas_50 = valor2 // 50
valor3 = valor2 - (notas_50 * 50)
notas_20 = valor3 // 20
valor4 = valor3 - (notas_20 * 20)
notas_10 = valor4 // 10
valor5 = valor4 - (notas_10 * 10)
notas_5 = valor5 // 5
valor6 = valor5 - (notas_5 * 5)
notas_2 = valor6 // 2
valor7 = valor6 - (notas_2 * 2)
notas_1 = valor7 // 1
print(valor)
print(notas_100, 'nota(s) de R$ 100,00')
print(notas_50, 'nota(s) de R$ 50,00')
print(notas_20, 'nota(s) de R$ 20,00')
print(notas_10, 'nota(s) de R$ 10,00')
print(notas_5, 'nota(s) de R$ 5,00')
print(notas_2, 'nota(s) de R$ 2,00')
print(notas_1, 'nota(s) de R$ 1,00')
'''

# 1019 Conversão de Tempo
'''
n = int(input())
horas = n // 3600
minutos = (n - (horas*3600)) // 60
segundos = n % 60
print(f'{horas}:{minutos}:{segundos}')
'''

# 1020 Idade em Dias
'''
total_dias = int(input())
ano = total_dias // 365
fator_ano = total_dias - (ano * 365)
mes = fator_ano // 30
dia = fator_ano % 30
print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
'''

# 1021 Notas e Moedas

meu_dinheiro = float(input())
notas = [200, 100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for nota in notas:
    quantidade_notas = int(meu_dinheiro / nota)
    print(f'{quantidade_notas} nota(s) de R$ {nota:.2f}')
    meu_dinheiro -= quantidade_notas * nota
print('MOEDAS:')
for moeda in moedas:
    quantidade_moedas = int(meu_dinheiro / moeda)
    print(f'{quantidade_moedas} moeda(s) de R$ {moeda:.2f}')
    meu_dinheiro -= quantidade_moedas * moeda

''' Solução da internet usando a mesma metodologia que usei no 1018
n = float(input())

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1
n1=float('%.2f'% n1)
n=float('%.2f'% n)

m50 = n // 0.5
n = n - m50*0.5
m50=float('%.2f'% m50)
n=float('%.2f'% n)

m25 = n // 0.25
n = n - m25*0.25
m25=float('%.2f'% m25)
n=float('%.2f'% n)

m10 = n // 0.10
n = n - m10*0.10
m10=float('%.2f'% m10)
n=float('%.2f'% n)

m5 = n // 0.05
n = n - m5*0.05
m5=float('%.2f'% m5)
n=float('%.2f'% n)

m1 = n * 100
m1=float('%.2f'% m1)
n=float('%.2f'% n)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(n1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m1)))
'''

#1035 Teste de Seleção
'''
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and (a % 2) != 1:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
'''

#1036 Formula de Bhaskara
'''
import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = (b * b) - 4 * a * c
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    bhaskara1 = (-b + math.sqrt(delta)) / (2 * a)
    bhaskara2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {bhaskara1:.5f}")
    print(f"R2 = {bhaskara2:.5f}")
'''

# 1037 Intervalo
'''
numero = float(input())

if 0 <= numero <= 25:
    print("Intervalo [0,25]")
elif 25 < numero <= 50:
    print("Intervalo (25,50]")
elif 50 < numero <= 75:
    print("Intervalo (50,75]")
elif 75 < numero <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
'''

# 1038 Lanche
'''
codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)
meu_dicionario_precos = {1 : 4.00, 2 : 4.50, 3 : 5.00, 4 : 2.00, 5 : 1.50}
valor = meu_dicionario_precos[codigo] * quantidade
print(f'Total: R$ {valor:.2f}')
'''

# 1040 Media 3
'''
n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1
media = ((n1 * peso1) + (n2 * peso2) + (n3 * peso3) + (n4 * peso4)) / (peso1 + peso2 + peso3 + peso4)
if media >= 7:
    print(f'Media: {media:.1f}')
    print("Aluno aprovado.")
elif 5.0 <= media < 7:
    exame = float(input())
    print(f'Media: {media:.1f}')
    print("Aluno em exame.")
    print(f'Nota do exame: {exame:.1f}')
    nova_media = (exame + media) / 2
    if nova_media >= 5:
        print("Aluno aprovado.")
        print(f'Media final: {nova_media:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {nova_media:.1f}')
else:
    print(f'Media: {media:.1f}')
    print("Aluno reprovado.")
'''
