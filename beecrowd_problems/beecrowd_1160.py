t = int(input())
for i in range(t):
    ano = 0
    pa, pb, g1, g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    while pa <= pb and ano <= 100:
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        ano += 1
        if ano > 100:
            break
    if ano > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{ano} anos.')
        