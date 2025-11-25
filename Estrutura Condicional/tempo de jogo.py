"""
Problema "tempo_de_jogo" (adaptado de URI 1046)
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
horas.
Exemplo 1:
Hora inicial: 16
Hora final: 2
O JOGO DUROU 10 HORA(S)
Exemplo 2:
Hora inicial: 0
Hora final: 0
O JOGO DUROU 24 HORA(S)
Exemplo 3:
Hora inicial: 2
Hora final: 16
O JOGO DUROU 14 HORA(S)

"""
h_inicial = int(input("Hora inicial: "))
h_final = int(input("Hora final: "))

if h_inicial < h_final:
    duracao = h_final - h_inicial 

else:
    duracao = 24 - h_final + h_inicial 

print(f"O JOGO DUROU {duracao} HORA(S)")