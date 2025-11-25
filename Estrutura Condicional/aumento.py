"""
Problema "aumento" (adaptado de URI 1048)
Uma empresa vai conceder um aumento percentual de salário aos seus 
funcionários dependendo de quanto cada pessoa ganha, conforme tabela ao 
lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento, quanto foi o aumento
e qual foi a porcentagem de aumento.
Salário atual Aumento
Até R$ 1000.00 20%
Acima de R$ 1000.00
até R$ 3000.00
15%
Acima de R$ 3000.00
até R$ 8000.00
10%
Acima de R$ 8000.00 5%
Exemplo 1:
Digite o salario da pessoa: 2500.00
Novo salario = R$ 2875.00
Aumento = R$ 375.00
Porcentagem = 15 %
Exemplo 2:
Digite o salario da pessoa: 8000.00
Novo salario = R$ 8800.00
Aumento = R$ 800.00
Porcentagem = 10 %

"""
salario_atual = float(input("Qual o seu salário?"))

if salario_atual <= 1000:
    porcentagem = 20

elif salario_atual <= 3000:
    porcentagem = 15

elif salario_atual <= 8000:
    porcentagem = 10

else:
    porcentagem = 5

aumento = salario_atual * (porcentagem / 100)
novo_salario = salario_atual + aumento

print(f"Novo salário = R${novo_salario:.2f}")
print(f"Aumento = R${aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")