"""
Problema "menor_de_tres"
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez.
Exemplo 1:
Primeiro valor: 7
Segundo valor: 3
Terceiro valor: 8
MENOR = 3

"""

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 < n2 and n1 < n3:
    print(f"MENOR = {n1}")

elif n2 < n1 and n2 < n3:
    print(f"MENOR = {n2}")
elif n3 < n1 and n3 < n2:
    print(f"MENOR = {n3}")
else:
    print(f"MENOR = {n1}")