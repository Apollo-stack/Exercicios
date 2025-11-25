tempo = int(input("Digite os segundos: "))

horas = tempo // 3600
tempo = tempo % 3600

minutos = tempo // 60
tempo = tempo % 60

segundos = tempo

print(f"{horas}:{minutos}:{segundos}")