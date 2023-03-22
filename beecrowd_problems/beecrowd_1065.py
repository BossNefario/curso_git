seq = 5
pares = 0
while seq > 0:
    n = int(input())
    if ((n % 2) == 0):
        pares += 1
        seq -= 1
    else:
        seq -= 1
print(pares,'valores pares')