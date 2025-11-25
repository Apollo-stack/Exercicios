#Meu código
salario = float(input("Qual o seu salário? "))


if salario <= 280:
    aumento = salario * (20 / 100) 
    salario_atual = salario + aumento
    print(f"Seu salário era R${salario:.2f}")
    print(f"Com um aumento de 20% ou seja R${aumento:.2f}")
    print(f"Seu novo salário é R${salario_atual:.2f}")

elif salario > 280 and salario <= 700:
    aumento = salario * (15 / 100) 
    salario_atual = salario + aumento
    print(f"Seu salário era R${salario:.2f}")
    print(f"Com um aumento de 15% ou seja R${aumento:.2f}")
    print(f"Seu novo salário é R${salario_atual:.2f}")

elif salario > 700 and salario <= 1500:
    aumento = salario * (10 / 100) 
    salario_atual = salario + aumento
    print(f"Seu salário era R${salario:.2f}")
    print(f"Com um aumento de 10% ou seja R${aumento:.2f}")
    print(f"Seu novo salário é R${salario_atual:.2f}")

else:
    aumento = salario * (5 / 100) 
    salario_atual = salario + aumento
    print(f"Seu salário era R${salario:.2f}")
    print(f"Com um aumento de 5% ou seja R${aumento:.2f}")
    print(f"Seu novo salário é R${salario_atual:.2f}")


#Código do Gemini
salario = float(input("Qual o seu salário? "))

# Variável para guardar o percentual
percentual = 0

# Lógica apenas para definir a regra
if salario <= 280:
    percentual = 20
elif salario <= 700: 
    # Dica de Ouro: Não precisa testar "salario > 280". 
    # Se o código chegou no elif, é ÓBVIO que ele é maior que 280, 
    # senão teria entrado no primeiro if.
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

# Processamento (cálculo) feito uma única vez
aumento = salario * (percentual / 100)
novo_salario = salario + aumento

# Saída de dados feita uma única vez
print(f"Salário original: R$ {salario:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")