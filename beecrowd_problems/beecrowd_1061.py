
# Leitura dos dados de entrada
dia_inicio = input().split()[1]
hora_inicio = input()
dia_fim = input().split()[1]
hora_fim = input()

# Conversão das strings para valores numéricos
hora_inicio = list(map(int, hora_inicio.split(":")))
hora_fim = list(map(int, hora_fim.split(":")))
dia_inicio = int(dia_inicio)
dia_fim = int(dia_fim)

# Cálculo da duração em segundos
total_segundos = (dia_fim - dia_inicio) * 86400  # 86400 segundos em um dia
total_segundos += (hora_fim[0] - hora_inicio[0]) * 3600  # 3600 segundos em uma hora
total_segundos += (hora_fim[1] - hora_inicio[1]) * 60  # 60 segundos em um minuto
total_segundos += hora_fim[2] - hora_inicio[2]

# Cálculo dos dias, horas, minutos e segundos
dias = total_segundos // 86400
total_segundos %= 86400
horas = total_segundos // 3600
total_segundos %= 3600
minutos = total_segundos // 60
total_segundos %= 60
segundos = total_segundos

# Impressão do resultado
print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(segundos))