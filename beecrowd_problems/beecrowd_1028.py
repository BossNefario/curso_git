import math

numero_de_testes = int(input())
temp = 0
while numero_de_testes > 0:
    a, b = map(int, input().split())
    mdc = math.gcd(a, b)
    print(mdc)
    numero_de_testes -= 1
