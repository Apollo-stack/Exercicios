saldo = float(500)
limite_cheque_especial = float(1000) 

print("Bem vindo")
print("")
print(f"Saldo total R${saldo:.2f}")
print(f"Seu limite de cheque especial é de R${limite_cheque_especial:.2f}")
print("")
saque = float(input("Qual valor deseja sacar?"))

if saque <= saldo:
    saldo_atual = saldo - saque 
    print(f"Saque Aprovado! ")
    print("")
    print(f"Saldo total: R${saldo_atual:.2f}")

elif saque < saldo + limite_cheque_especial:
    saldo_atual = - saque - saldo + limite_cheque_especial 
    print(f"Saque aprovado!")
    print(f"ATENÇÃO! Limite de chque especial foi usado")
    print("")
    print(f"Saldo total: R${saldo_atual:.2f}")

elif saque > saldo + limite_cheque_especial:
    print("Saque Negado! Saldo insuficiente!")