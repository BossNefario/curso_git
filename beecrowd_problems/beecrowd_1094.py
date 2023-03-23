numero = int(input())
total_coelho = 0
total_rato = 0
total_sapo = 0
total = 0
while numero > 0:
    qtde, tipo = input().split()
    qtde = int(qtde)
    total += qtde
    numero -= 1
    if tipo == 'C':
        qtde_coelho = qtde
        total_coelho += qtde_coelho
    elif tipo == 'R':
        qtde_rato = qtde
        total_rato += qtde_rato
    else:
        qtde_sapo = qtde
        total_sapo += qtde_sapo

per_coelho = (total_coelho / total) * 100
per_rato = (total_rato / total) * 100
per_sapo = (total_sapo / total) * 100
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_coelho}')
print(f'Total de ratos: {total_rato}')
print(f'Total de sapos: {total_sapo}')
print(f'Percentual de coelhos: {per_coelho:.2f} %')
print(f'Percentual de ratos: {per_rato:.2f} %')
print(f'Percentual de sapos: {per_sapo:.2f} %')