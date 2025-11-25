"""
Problema "pagamento"
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo.
Exemplo 1:
Nome: Joao Silva
Valor por hora: 50.00
Horas trabalhadas: 60
O pagamento para Joao Silva deve ser 3000.00

"""

nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
hora_trab = int(input("Horas trabalhadas: "))

pag = valor_hora * hora_trab

print(f"O pagamento para {nome} deve ser R${pag:.2f}")