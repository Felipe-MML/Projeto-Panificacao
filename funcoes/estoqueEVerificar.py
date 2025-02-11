import json
import os

arquivo_json = "produtos.json"

# Verifica se o arquivo existe, se não cria um arquivo vazio.
if not os.path.exists(arquivo_json):
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump([], arquivo)

# Carregar dados:
def carregar_dados():
    with open(arquivo_json, "r", encoding='utf-8') as arquivo:
        return json.load(arquivo)

# Salvar dados
def salvar_dados(dados):
    with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

# Adicionar novos produtos
def adicionar_informacao():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()

    visualizar_estoque()

    print("\n=== Adicionar Matéira Prima ===")
    try:
        cod = int(input("Código do produto: "))
    except ValueError:
        print("Erro: O código do produto precisa ser um número inteiro.")
        return
    
    # Verificação se já há o item no estoque
    for item in dados:
        if item["cod"] == cod:
            quantidade = int(input('Quantidade à adicionar: '))
            nome = item['nome']
            item["quantidade"] += quantidade
            print(f"Quantidade de {nome}, atualizada para {item['quantidade']}")

            salvar_dados(dados)
            return
    try:
        nome = input("Tipo do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input('Quantidade à adicionar: '))
    except ValueError:
        print('ERRO: O preço e a quantidade precisam ser números')
        return
        
    novo_registro = {"nome": nome, "cod": cod, "preço": preco, "quantidade": quantidade}
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Produto adicionado com sucesso!")
        

# Visualizar o estoque
def visualizar_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    if dados:
            print("\n=== Estoque ===")
            for i, item in enumerate(dados, 1):
                print(f"{i}.COD: {item['cod']}, Tipo: {item['nome']}, Preço: {item['preço']}, Quantidade: {item['quantidade']}")
    else: 
        print('Nenhuma informação salva ainda')

# Deletar do estoque
def deletar_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    
    if not dados:
        print("O estoque está vazio!")
        return

    visualizar_estoque()  
    
    try:
        cod = int(input("\nDigite o código do produto a ser removido: "))
    except ValueError:
        print("Erro: O código deve ser um número inteiro.")
        return

    
    novos_dados = [item for item in dados if item["cod"] != cod]

    if len(novos_dados) == len(dados):
        print("Erro: Produto não encontrado!")
        return

    salvar_dados(novos_dados)
    print("Matéria prima removida com sucesso!")

# Editar um item do estoque 
def editar_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    
    if not dados:
        print("O estoque está vazio!")
        return

    visualizar_estoque()

    try:
        cod = int(input("\nDigite o código do produto a ser editado: "))
    except ValueError:
        print("Erro: O código deve ser um número inteiro.")
        return

    for item in dados:
        if item["cod"] == cod:
            print("\nDeixe em branco para manter o valor atual.")

            novo_nome = input(f"Novo nome ({item['nome']}): ") or item['nome']
            novo_preco = input(f"Novo preço ({item['preço']}): ")
            nova_quantidade = input(f"Nova quantidade ({item['quantidade']}): ")

            # Converte os valores, se forem informados
            item["nome"] = novo_nome if novo_nome else item['nome']
            item["preço"] = float(novo_preco) if novo_preco else item["preço"]
            item["quantidade"] = int(nova_quantidade) if nova_quantidade else item["quantidade"]

            salvar_dados(dados)
            print("Produto atualizado com sucesso!")
            return

    print("Erro: Produto não encontrado!")
