novo_grenal = 1
vi = 0
vg = 0
grenais = 0
empate = 0
while True:
    if novo_grenal != 2:
        gi, gg = map(int, input().split())
        if gi > gg:
            vi += 1
            grenais += 1
            print('Novo grenal (1-sim 2-nao)')
            novo_grenal = int(input())
        elif gg > gi:
            vg += 1
            grenais += 1
            print('Novo grenal (1-sim 2-nao)')
            novo_grenal = int(input())
        else:
            empate += 1
            grenais += 1
            print('Novo grenal (1-sim 2-nao)')
            novo_grenal = int(input())
    else:
        break
print(grenais, 'grenais')
print(f'Inter:{vi}')
print(f'Gremio:{vg}')
print(f'Empates:{empate}')
if vi > vg:
    print('Inter venceu mais')
elif vg > vi:
    print('Gremio venceu mais')
else:
    print("Nao houve vencedor")