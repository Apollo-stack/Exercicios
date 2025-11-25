"""
Problema "dardo"
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior.
Exemplo 1:
Digite as tres distancias:
83.21
79.53
89.15
MAIOR DISTANCIA = 89.15
Exemplo 2:
Digite as tres distancias:
83.21
87.20
83.21
MAIOR DISTANCIA = 87.20

"""
print("Digite as três distâncias:")
d1 = float(input())
d2 = float(input())
d3 = float(input())

if d1 > d2 and d1 > d3:
    print(f"MAIOR DISTÂNCIA = {d1}")
elif d2 > d3:
    print(f"MAIOR DISTÂNCIA = {d2}")
else:
    print(f"MAIOR DISTÂNCIA = {d3}")