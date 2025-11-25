"""
Problema "duracao"
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.
Exemplo 1:
Digite a duracao em segundos: 300
0:5:0

"""
seg = int(input("Digite a duração em segundos: "))

horas = seg // 3600
resto = seg % 3600
minutos = resto / 60
segundos = resto % 60

print(f"{horas}:{int(minutos)}:{segundos}")
