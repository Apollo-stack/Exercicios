"""
Problema "dentro_fora" (adaptado de URI 1072)
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
conforme exemplo
Exemplo:
Quantos numeros voce vai digitar? 5
Digite um numero: 14
Digite um numero: 35
Digite um numero: 10
Digite um numero: 131
Digite um numero: 8
2 DENTRO
3 FORA

"""

n = int(input("Quantos números você vai digitar? "))

dentro = 0
fora = 0

for i in range (n):
    numero = int(input("Digite um número: "))
    if numero >= 10 and numero <= 20:
        dentro = dentro + 1
    else: 
        fora = fora + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")