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

total_dias = int(input())
ano = total_dias // 365
fator_ano = total_dias - (ano * 365)
mes = fator_ano // 30
dia = fator_ano % 30
print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")