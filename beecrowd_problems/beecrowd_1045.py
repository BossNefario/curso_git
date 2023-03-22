'''
a, b, c = list(map(float, input().split()))
if a < b:
    temp = a
    a = b
    b = temp
if b < c:
    temp = b
    b = c
    c = temp
if a < b:
    temp = a
    a = b
    b = temp
print (a, b, c)
soma = b + c
quadrado_a = a * a
soma_dos_quadrados = (b ** 2) + (c ** 2)
if a >= soma:
    print('NAO FORMA TRIANGULO')
elif quadrado_a == soma_dos_quadrados:
    print('TRIANGULO RETANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
    else:
        pass
elif quadrado_a > soma_dos_quadrados:
    print('TRIANGULO OBTUSANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
    else:
        pass
else:
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
    else:
        pass
'''

'''
a,b,c=list(map(float,input().split()))
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if(a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif(a*a == (b*b+c*c)):
     print("TRIANGULO RETANGULO")
elif(a * a > (b*b+ c*c)):
    print("TRIANGULO OBTUSANGULO")
elif(a*a<(b*b + c*c)):
    print("TRIANGULO ACUTANGULO")
if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
elif(a == b or b == c):
        print("TRIANGULO ISOSCELES")
'''