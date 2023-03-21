salario = float(input())
if salario > 2000.00:
    reajuste = salario * 0.04
    salario += reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 4 %')
elif salario > 1200.00:
    reajuste = salario * 0.07
    salario += reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 7 %')
elif salario > 800.00:
    reajuste = salario * 0.10
    salario += reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 10 %')
elif salario > 400.00:
    reajuste = salario * 0.12
    salario += reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 12 %')
else:
    reajuste = salario * 0.15
    salario += reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 15 %')