"""
Problema "consumo"
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.
Exemplo 1:
Distancia percorrida: 500
Combustível gasto: 38.5
Consumo medio = 12.987

"""

d_percorrida = int(input("Distância percorrida (km): "))
c_gasto = float(input("Combustível gasto: "))

media = d_percorrida / c_gasto 

print(f"Consumo medio = {media:.3f}")