'''
numero = int(input())
people = []
while numero > 0:
    nome, sobrenome, idade, sexo = input().split()
    idade = int(idade)
    if sexo == 'F':
        arg = 'Ms.'
    else:
        arg = 'Mr.'
    minha_tupla = (arg, nome, sobrenome, idade, sexo)
    people.append(minha_tupla)
    sorted_people = sorted(people, key=lambda x: (x[3], x[1], x[2]))
    numero -= 1
for i in sorted_people:
    print(i[0], i[1], i[2])
'''
