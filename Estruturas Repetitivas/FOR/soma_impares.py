"""  
Problema "soma_impares" (adaptado de URI 1071)
Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
impares entre eles.
Exemplo 1:
Digite dois numeros:
2
9
SOMA DOS IMPARES = 15
Exemplo 2:
Digite dois numeros:
15
10
SOMA DOS IMPARES = 24
Exemplo 3:
Digite dois numeros:
6
-5
SOMA DOS IMPARES = 5

"""

print("Digite dois numeros")
x = int(input())
y = int(input())



if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range (x +1 and y):
    if i % 2 != 0:
        soma = soma + 1


print(soma)