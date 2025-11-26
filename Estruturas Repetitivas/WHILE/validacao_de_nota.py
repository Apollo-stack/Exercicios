"""  
Problema "validacao_de_nota" (adaptado de URI 1117)
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
intervalo [0,10]). Cada nota deve ser validada separadamente.
Exemplo 1:
Digite a primeira nota: 3.5
Digite a segunda nota: 10.0
MEDIA = 6.75
Exemplo 2:
Digite a primeira nota: -3.5
Valor invalido! Tente novamente: 3.5
Digite a segunda nota: 11.0
Valor invalido! Tente novamente: 10.5
Valor invalido! Tente novamente: 10.0
MEDIA = 6.75

"""



n1 = float(input("Digite a primeira nota: "))
while n1 <= 0 or n1 > 10:
    n1 = float(input("Valor invalido! Tente novamente: "))

        
n2 = float(input("Digite a segunda nota: "))
while n2 <= 0 or n2 >10:
    n2 = float(input("Valor invalido! Tente novamente: "))

media = (n1 + n2) / 2
print(f"MEDIA = {media:4.2f}")