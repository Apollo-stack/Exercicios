valor = int(input("Quanto você quer sacar? R$ "))

# Notas de 100
notas_100 = valor // 100
valor = valor % 100  # Atualizamos o valor com o que sobrou (o resto)

# Notas de 50
notas_50 = valor // 50
valor = valor % 50   # O que sobrar daqui vai para a próxima checagem

# Notas de 10
notas_10 = valor // 10
valor = valor % 10

# Notas de 5
notas_5 = valor // 5
valor = valor % 5

# Notas de 1
notas_1 = valor # O que sobrar no final são as moedas de 1

print(f"Notas de 100: {notas_100}")
print(f"Notas de 50:  {notas_50}")
print(f"Notas de 10:  {notas_10}")
print(f"Notas de 5:   {notas_5}")
print(f"Notas de 1:   {notas_1}")