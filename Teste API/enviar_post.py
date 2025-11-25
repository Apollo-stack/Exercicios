import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Este é o pacote que vamos enviar (Dicionário Python)
meu_pacote = {
    "title": "Dominando APIs com Python",
    "body": "Acabei de aprender a baixar imagens e agora estou enviando dados.",
    "userId": 1
}

print("Enviando dados para o servidor...")

# A MÁGICA ACONTECE AQUI
# Usamos .post() em vez de .get()
# O parâmetro 'json=' avisa o Python: "Formate esse dicionário automaticamente e mande como JSON"
response = requests.post(url, json=meu_pacote)

# Verificando
if response.status_code == 201: # 201 = Criado com sucesso
    print("\n--- SUCESSO! DADO CRIADO ---")
    print("O servidor respondeu com:")
    print(response.json())
else:
    print(f"Erro: {response.status_code}")