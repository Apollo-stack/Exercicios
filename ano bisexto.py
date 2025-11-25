ano = int(input("Digite um ano: "))


if (ano % 400 == 0) or ((ano % 4 == 0)  and (not ano % 100 == 0)):
    print(f"O ano {ano} é bissexto")
else:
    print("Não é bissexto")