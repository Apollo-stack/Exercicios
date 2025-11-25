"""
Problema "lanchonete" (adaptado de URI 1038)
Uma lanchonete possui vários produtos. Cada produto possui um código
e um preço. Você deve fazer um programa para ler o código e a
quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais, conforme
tabela de produtos ao lado.
Código do
produto
Preço do
produto
1 R$ 5.00
2 R$ 3.50
3 R$ 4.80
4 R$ 8.90
5 R$ 7.32
Exemplo 1:
Codigo do produto comprado: 1
Quantidade comprada: 3
Valor a pagar: R$ 15.00
Exemplo 2:
Codigo do produto comprado: 4
Quantidade comprada: 2
Valor a pagar: R$ 17.80

"""

cod_produto = int(input("Digite o código do produto: "))
quantidade_comprada = int(input("Informe a quantidade comprada: "))

match cod_produto:
    case 1:
        valor_final = quantidade_comprada * 5
        print(f"Valor a pagar = R${valor_final:.2f}")
    
    case 2:
        valor_final = quantidade_comprada * 3.50
        print(f"Valor a pagar = R${valor_final:.2f}")

    case 3:
        valor_final = quantidade_comprada * 4.80
        print(f"Valor a pagar = R${valor_final:.2f}")

    case 4:
        valor_final = quantidade_comprada * 8.90
        print(f"Valor a pagar = R${valor_final:.2f}")

    case 5:
        valor_final = quantidade_comprada * 7.32
        print(f"Valor a pagar = R${valor_final:.2f}")