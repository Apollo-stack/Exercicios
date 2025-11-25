"""
Problema "medidas"
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
Exemplo 1:
Digite a medida A: 4.0
Digite a medida B: 3.5
Digite a medida C: 5.2
AREA DO QUADRADO = 16.0000
AREA DO TRIANGULO = 7.0000
AREA DO TRAPEZIO = 19.5000

"""

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

area_quadrado = a * a
area_triangulo = a * b / 2
area_trapezio = (a + b) * c / 2

print(f"AREA DO QUADRADO = {area_quadrado:.4f}") 
print(f"AREA DO TRIÂNGULO = {area_triangulo:.4f}") 
print(f"AREA DO TRAPÉZIO = {area_trapezio:.4f}") 