"""
Problema "multiplos" (adaptado de URI 1044)
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
números podem ser digitados em qualquer ordem.
Exemplo 1:
Digite dois numeros inteiros:
6
24
Sao multiplos
Exemplo 2:
Digite dois numeros inteiros:
24
6
Sao multiplos

"""
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

divisao1 = n1 / n2
divisao2 = n2 / n1

if divisao1 % 2 == 0 or divisao2 % 2 == 0:
   print("São multiplos.")
else:
   print("Não são multiplos.")