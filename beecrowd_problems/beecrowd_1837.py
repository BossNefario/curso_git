import math

a, b = input().split()
a = int(a)
b = int(b)
if b >= 0:
    quociente = a // b
    resto = a % b
else:
    quociente = (a // b) + 1
    resto = a - (b * quociente)
print(quociente, resto)
