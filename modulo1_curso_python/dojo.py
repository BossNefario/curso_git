def converter_romanos(num):
  
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  

    milhares = m[num // 1000]
    centenas = c[(num % 1000) // 100]
    dezenas = x[(num % 100) // 10]
    unidades = i[num % 10]
  
    resposta = (milhares + centenas + dezenas + unidades)
  
    return resposta
  
numero = int(input("Digite um número: "))
print(converter_romanos(numero))