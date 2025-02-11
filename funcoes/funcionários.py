import json
import os

arquivo3_json = 'funcionarios.json'

if not os.path.exists(arquivo3_json):
    with open(arquivo3_json, "w", encoding="utf-8") as arquivo3:
        json.dump([], arquivo3)

def carregar_dados():
    with open(arquivo3_json, "r", encoding='utf-8') as arquivo3:
        return json.load(arquivo3)
    
def salvar_dados(dados):
    with open(arquivo3_json, 'w', encoding='utf-8') as arquivo3:
        json.dump(dados, arquivo3, ensure_ascii=False, indent=4)

# Registro de funcionários
def registrar_funcionarios():
        os.system('cls' if os.name == 'nt' else 'clear')
        dados = carregar_dados()

        visualizar_funcionarios()

        print("\n=== Adicionar Funcionário ===")
        try:
            cpf = int(input('Digite o CPF: '))
            for item in dados:
                if item["cpf"] == cpf:
                    print(f"O cpf {cpf} já foi registrado!")

                    salvar_dados(dados)
                    return
        
            nome = input("Informe o nome do funcionário: ")
            cargo = input("Informe o cargo: ")
            salario = float(input("Informe o salário: "))

        except ValueError:
            print('O cpf e o salário precisam ser valores numéricos!')
            return

        
        novo_registro = {"Nome": nome, "cargo": cargo, "salario": salario, "cpf": cpf}
        dados.append(novo_registro)
        salvar_dados(dados)
        print("Funcionário cadastrado!")

# Visualização de funcionários
def visualizar_funcionarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    if dados:
        print("\n=== Funcionários ===")
        for i, item in enumerate(dados, 1):
            print(f"{i}.CPF: {item['cpf']}, Nome: {item['Nome']}, Cargo: {item['cargo']}, Salário: {item['salario']}")
    else: 
        print('Nenhuma informação salva ainda')

# Edição de funcionários
def editar_funcionarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()

    if not dados:
        print('Não há funcionários registrados')
        return
    
    visualizar_funcionarios()

    try:
        cpf = int(input("\nDigite o cpf do funcionário a ser editado: "))
    except ValueError:
        print("Erro: O CPF deve ser um número inteiro.")
        return
    
    for item in dados: 
        if item["cpf"] == cpf:
            print("\nDeixe em branco para manter o valor atual.")

            novo_nome = input(f"Novo nome ({item['Nome']}): ") or item ['Nome']
            novo_cargo = input(f"Novo cargo ({item['cargo']}): ")
            novo_salario = input(f"Novo salário ({item['salario']}): ")

            # Converter os valores
            item["Nome"] = novo_nome if novo_nome else item['Nome']
            item["cargo"] = novo_cargo if novo_cargo else item["cargo"]
            item["salario"] = float(novo_salario)  if novo_salario else item["salario"]

            salvar_dados(dados)
            print("Funcionário atualizado com sucesso!")
            return
    print("Erro: CPF não encontrado!")

# Deletar funcionário
def deletar_funcionario():
    os.system('cls' if os.name == 'nt' else 'clear')
    dados = carregar_dados()
    
    if not dados:
        print("Sem funcionários para deletar!")
        return

    visualizar_funcionarios()  
    
    try:
        cpf = int(input("\nDigite o CPF do funcionário que deseja deletar: "))
    except ValueError:
        print("Erro: O cpf deve ser um número inteiro.")
        return
    
    novos_dados = [item for item in dados if item["cpf"] != cpf]

    if len(novos_dados) == len(dados):
        print("Erro: Produto não encontrado!")
        return

    salvar_dados(novos_dados)
    print("Funcionário removido com sucesso!")