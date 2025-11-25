"""
Problema "operadora"
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.
Exemplo 1:
Digite a quantidade de minutos: 22
Valor a pagar: R$ 50.00

"""

minutos = int(input("Digite a quantidade de minutos: "))

minutos_excedido = minutos - 100
pagar_excedido = minutos_excedido * 2 + 50

if minutos <= 100:
    print(f"Valor a pagar: R$50,00")

else:
    print(f"Valor a pagar R${pagar_excedido:.2f}")