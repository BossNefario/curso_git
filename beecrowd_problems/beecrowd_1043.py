a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
minha_lista = [a, b, c]
minha_lista = sorted(minha_lista)
if minha_lista[0] + minha_lista[1] > minha_lista[2]:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a + b) / 2 * c
    print(f'Area = {area:.1f}')
