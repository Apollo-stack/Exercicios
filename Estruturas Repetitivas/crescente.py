"""
Problema "crescente" (adaptado de URI 1113)
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais.
Exemplo:
Digite dois numeros:
5
4
DECRESCENTE!
Digite outros dois numeros:
3
8
CRESCENTE!
Digite outros dois numeros:
2
2

"""


x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

while x != y:
    if x > y:
        print("DECRESCENTE!")
    else:
        print("CRESCENTE!")
    
    x = int(input("Digite novamente o primeiro número: "))
    y = int(input("Digite novamente o segundo número: "))

else:
    print("Os valores são iguais.")