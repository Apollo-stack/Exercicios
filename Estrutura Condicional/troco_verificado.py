"""
Problema "troco_verificado"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante conforme exemplo.
Exemplo 1:
Preço unitário do produto: 8.00
Quantidade comprada: 2
Dinheiro recebido: 20.00
TROCO = 4.00

"""

preco_produto = float(input("Preço unitário de produto: "))
qtd_comprada = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))

troco = preco_produto * qtd_comprada - recebido 



if recebido < troco:
    print(f"Dinheiro insuficiente, faltam R${troco:.2f}!")

else:
    print(f"TROCO = R${troco:.2f}")

    