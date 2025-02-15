import json
import os
from datetime import datetime

arquivo2_json = "cardapio.json"

if not os.path.exists(arquivo2_json):
    with open(arquivo2_json, "w", encoding="utf-8") as arquivo2:
        json.dump([], arquivo2)

def carregar_dados():
    with open(arquivo2_json, "r", encoding='utf-8') as arquivo2:
        return json.load(arquivo2)

def salvar_dados(dados):
    with open(arquivo2_json, 'w', encoding='utf-8') as arquivo2:
        json.dump(dados, arquivo2, ensure_ascii=False, indent=4)

def adicionar_produto():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()

    visualizar_cardapio()

    print("\n=== Adicionar ao catálogo ===")
    try:
        cod = int(input("Código do produto: "))
    except ValueError:
        print('Erro: O código do produto precisa ser um número inteiro.')
        return

    # Verificação se já há o produto no catálogo

    for item in dados:
        if item["cod"] == cod:
            quantidade = int(input('Quantidade à adicionar: '))
            nome = item['Nome']
            item["quantidade"] += quantidade
            print(f"Quantidade de {nome}, atualizada para {item['quantidade']}")

            salvar_dados(dados)
            return
        
    nome = input("Nome do produto: ")
    preço = float(input("Preço do produto: "))
    quantidade = int(input('Quantidade à adicionar: '))
    
        
    novo_registro = {"cod": cod, "Nome": nome, "preço": preço, "quantidade": quantidade}
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Produto adicionado com sucesso!")

# Visualizar o catálogo
def visualizar_cardapio():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    if dados:
            print("\n=== catálogo ===")
            for i, item in enumerate(dados, 1):
                print(f"{i}. COD: {item['cod']} Nome: {item['Nome']}, Preço: {item['preço']}, Quantidade: {item['quantidade']}")
    else: 
        print('Nenhuma informação salva ainda')

# Deletar produto do catálogo:
def deletar_produto():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    
    if not dados:
        print("O catálogo está vazio!")
        return

    visualizar_cardapio()  
    
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
    print("Produto removido com sucesso!")


# Executar uma venda
def vender_produto():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    if not dados:
        print("Nenhum produto disponível.")
        return
    
    visualizar_cardapio()  

    try:
        cod = int(input("Digite o código do produto: "))
        quantidade = int(input("Quantidade: "))
        dataEHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    except ValueError:
        print("Erro: Código e quantidade devem ser números inteiros.")
        return
    
    produto = next((item for item in dados if item["cod"] == cod), None)
    
    if not produto:
        print("Erro: Produto não encontrado.")
        return
    
    if produto["quantidade"] < quantidade:
        print("Erro: Estoque insuficiente!")
        return
    
    produto["quantidade"] -= quantidade
    total = produto['preço'] * quantidade
    print(f"Venda realizada: {quantidade}x {produto['Nome']} por R${total:.2f}")
    
    salvar_dados(dados)
    salvar_historico_compras(cod, produto['Nome'], quantidade, total, dataEHora)

# Histórico de compras
def salvar_historico_compras(cod, nome, quantidade, total, dataEHora):
    historico = []
    try:
        with open("historico_compras.json", "r", encoding="utf-8") as file:
            historico = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    historico.append({
        "cod": cod,
        "nome": nome,
        "quantidade": quantidade,
        "total": total,
        "dataEHora": dataEHora
    })
    
    with open("historico_compras.json", "w", encoding="utf-8") as file:
        json.dump(historico, file, indent=4, ensure_ascii=False)

# Visualizar o Histórico de compras
arquivoHistorico_json = 'historico_compras.json'

if not os.path.exists(arquivoHistorico_json):
    with open(arquivoHistorico_json, "w", encoding="utf-8") as arquivoHistorico:
        json.dump([], arquivoHistorico)

def carregarHistorio():
    with open(arquivoHistorico_json, "r", encoding='utf-8') as arquivoHistorico:
        return json.load(arquivoHistorico)

def visualizar_historico():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregarHistorio()
    if dados:
        print('\n === Histórico de Compras ===')
        for i, item in enumerate(dados, 1):
            print(f"Produto: {item['nome']} | Total: {item['total']} | Data e hora da compra: {item['dataEHora']}")
    else:
        print('Nada registrado no histórico :()')

