"""
Problema "baskara"
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
Exemplo 1:
Coeficiente a: 1
Coeficiente b: 0
Coeficiente c: -9
X1 = 3.0000
X2 = -3.0000
Exemplo

"""
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Não é equação de segundo grau!")
else:
    # Correção 1: Fórmula correta (4 * a * c)
    delta = b ** 2 - 4 * a * c 

    # Correção 2: Toda essa lógica fica DENTRO do else.
    # Se a for 0, nada disso acontece.
    if delta < 0:
        print("A equação não possui raízes reais!")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"Raiz única: {raiz:.2f}")
    else:
        # Correção 3: Calcular x1 e x2 separadamente
        raiz1 = (-b + delta ** 0.5) / (2 * a)
        raiz2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Raiz 1: {raiz1:.2f}")
        print(f"Raiz 2: {raiz2:.2f}")