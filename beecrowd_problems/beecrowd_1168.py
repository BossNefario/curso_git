qtde = int(input())
while qtde > 0:    
    numero = input()
    leds = 0
    for caractere in numero:
        if caractere == '8':
            leds += 7
        elif caractere == '9' or caractere == '6' or caractere == '0':
            leds += 6
        elif caractere == '5' or caractere == '2' or caractere == '3':
            leds += 5
        elif caractere == '4':
            leds += 4
        elif caractere == '7':
            leds += 3
        else:
            leds += 2
    print(leds, 'leds')
    qtde -= 1
