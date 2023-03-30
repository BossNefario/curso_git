seq = 0
while seq < 100:
    numero = float(input())
    if numero <= 10:
        print(f'A[{seq}] = {numero:.1f}')
        seq += 1
    else:
        seq += 1