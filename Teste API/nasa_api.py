import requests

url = "https://api.nasa.gov/planetary/apod"
chave_secreta = "DEMO_KEY"

parametros = {
    "api_key": chave_secreta
}

print("Contatando a NASA...")

response = requests.get(url, params=parametros)

# --- ÁREA DE INVESTIGAÇÃO ---
print(f"Status Code recebido: {response.status_code}")
print("--- Início da Resposta Bruta ---")
print(response.text) # <--- Isso vai nos mostrar o que veio de verdade
print("--- Fim da Resposta Bruta ---")
# -----------------------------

if response.status_code == 200:
    try:
        dados = response.json()
        print("\n--- SUCESSO! ---")
        print(f"Título: {dados['title']}")
        print(f"URL: {dados['url']}")

        # --- NOVO BLOCO: BAIXANDO A IMAGEM ---
        url_imagem = dados['url']
        
        # Fazemos um novo pedido, agora para a URL da imagem
        resposta_imagem = requests.get(url_imagem)

        if resposta_imagem.status_code == 200:
            # Abre um arquivo chamado 'foto_nasa.jpg' no modo 'wb' (Write Binary)
            with open("foto_nasa.jpg", "wb") as arquivo:
                arquivo.write(resposta_imagem.content) # .content é para arquivos, .text é para texto
            print("\nImagem salva com sucesso na sua pasta!")
        else:
            print("Erro ao baixar a imagem.")

        
    except:
        print("\nO status foi 200, mas o conteúdo não era JSON válido.")
else:
    print(f"\nOps! Algo deu errado. Código: {response.status_code}")