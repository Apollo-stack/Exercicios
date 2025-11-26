"""
Problema "par_impar" (adaptado de URI 1074)
Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
apenas NULO.
Exemplo:
Quantos numeros voce vai digitar? 4
Digite um numero: -5
IMPAR NEGATIVO
Digite um numero: 0
NULO
Digite um numero: 3
IMPAR POSITIVO
Digite um numero: -4
PAR NEGATIVO

"""

n = int(input("Quantos números você vai digitar? "))

for i in range (1, n+1):
    numero = int(input("Digite um número: "))
    impar = numero % 2 != 0
    par = numero % 2 == 0

    if numero < 0 and impar:
        print("IMPAR NEGATIVO")

    elif numero > 0 and impar:
        print("IMPAR POSITIVO")
    
    elif numero < 0 and par:
        print("PAR NEGATIVO")
    elif numero > 0 and par:
        print("PAR POSITIVO")
    else:
        print("NULO")


#outra opção (pelo curso)

n = int(input("Quantos números você vai digitar? "))

for i in range (1, n+1):
    x = int(input("Digite um número: "))

    if x == 0:
        print("NULO")

    elif x % 2 == 0:
        if x < 0:
            print("PAR NEGATIVO")
        else:
            print("PAR POSITIVO")
    else:
        if x < 0:      
            print("IMPAR NEGATIVO")
        else:
            print("IMPAR POSITIVO")  

    