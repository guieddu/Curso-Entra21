hora = float(input("Informe a hora, em horas: "))
minuto = float(input("Informe o minuto, em minutos: "))
segundos = float(input("Informe os segundos, em segundos: "))
hora_segundo = hora*3600
minuto_segundo = minuto*60
soma = segundos+hora_segundo+minuto_segundo
print(f"A soma total das horas, minutos e segundos deu {soma} em segundos")