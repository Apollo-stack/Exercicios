import requests

pokemon = input("Digite o nome de um Pokemon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    nome = dados['name']
    
    print(f"\n--- {nome.upper()} ---")
    
    # Lista de Habilidades
    print("Habilidades:")
    
    # O 'dados['abilities']' é a lista completa.
    # Chamamos cada pedacinho dessa lista de 'item'
    for item in dados['abilities']:
        habilidade = item['ability']['name']
        print(f" -> {habilidade}")
        
else:
    print("Pokémon não encontrado!")