renda = float(input())
if renda > 4500.00:
    imposto = (renda - 4500.00) * 0.28
    imposto += (4500.00 - 3000 + 0.01) * 0.18
    imposto += (3000.00 - 2000 + 0.01) *0.08
    print(f'R$ {imposto:.2f}')
elif renda > 3000.00:
    imposto = (renda - 3000 + 0.01) * 0.18
    imposto += (3000.00 - 2000 + 0.01) * 0.08
    print(f'R$ {imposto:.2f}')
elif renda > 2000.00:
    imposto = (renda - 2000 + 0.01) * 0.08
    print(f'R$ {imposto:.2f}')
else:
    print('Isento')   

