"""
Problema "notas"
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO", conforme exemplos.
Exemplo 1:
Digite a primeira nota: 45.5
Digite a segunda nota: 31.3
NOTA FINAL = 76.8
Exemplo

"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

final = nota1 + nota2

if final >= 60.00:
    print(f"NOTA FINAL: {final:.1f}" )
    print("APROVADO!")
else:
     print(f"NOTA FINAL: {final:.1f}" )
     print("REPROVADO!")
