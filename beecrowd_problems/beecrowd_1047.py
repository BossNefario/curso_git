hora_inicio, minuto_inicio, hora_termino, minuto_termino = map(int, input().split())
dia = 24
hora = 60

if hora_inicio < hora_termino and minuto_inicio <= minuto_termino:
    resultado_hora = hora_termino - hora_inicio 
    resultado_minuto = minuto_termino - minuto_inicio
elif hora_inicio < hora_termino and minuto_inicio > minuto_termino:
    resultado_hora = hora_termino - hora_inicio - 1
    parcial_minuto = hora - minuto_inicio
    resultado_minuto = parcial_minuto + minuto_termino
elif hora_inicio > hora_termino and minuto_inicio <= minuto_termino:
    parcial_hora = dia - hora_inicio
    resultado_hora = parcial_hora + hora_termino
    resultado_minuto = minuto_termino - minuto_inicio
elif hora_inicio > hora_termino and minuto_inicio > minuto_termino:
    parcial_hora = dia - hora_inicio
    resultado_hora = parcial_hora + hora_termino - 1
    parcial_minuto = hora - minuto_inicio
    resultado_minuto = parcial_minuto + minuto_termino
elif hora_inicio == hora_termino and minuto_inicio < minuto_termino:
    resultado_hora = hora_termino - hora_inicio 
    resultado_minuto = minuto_termino - minuto_inicio
elif hora_inicio == hora_termino and minuto_inicio > minuto_termino:
    resultado_hora = dia - 1
    parcial_minuto = hora - minuto_inicio
    resultado_minuto = parcial_minuto + minuto_termino
else:
    resultado_hora = dia
    resultado_minuto = 0
print(f'O JOGO DUROU {resultado_hora} HORA(S) E {resultado_minuto} MINUTO(S)')  
