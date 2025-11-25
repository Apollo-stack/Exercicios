"""
Problema "temperatura"
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve
deduzir a fórmula de Celsius para Fahrenheit): ( 32)
9
5 C  F 
Exemplo 1:
Voce vai digitar a temperatura em qual escala (C/F)? F
Digite a temperatura em Fahrenheit: 75.00
Temperatura equivalente em Celsius: 23.89
Exemplo 2:
Voce vai digitar a temperatura em qual escala (C/F)? C
Digite a temperatura em Celsius: 28.15
Temperatura equivalente em Fahrenheit: 82.67

"""

escala = input("Você vai digitar a temperatura em qual escala (C/F)?")

if escala == 'F':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    conversao = 5 / 9 (f - 32)
    print(f"Temperatura equivalente em Celsius: {conversao:.2f}")

elif escala == 'C':
    c = float(input("Digite a temperatura em Celsius: "))
    conversao = 5 / 9 (c - 32)
    print(f"Temperatura equivalente em Fahrenheit: {conversao:.2f}")