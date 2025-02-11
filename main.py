from funcoes import adicionar_informacao, visualizar_estoque, adicionar_produto, visualizar_cardapio, registrar_funcionarios, visualizar_funcionarios, vender_produto, visualizar_historico, deletar_produto, deletar_estoque, editar_estoque, editar_funcionarios, deletar_funcionario
import os

# Menu
def menuGerente():
    while True:
        print('\n=== Menu ===')

        print('\n01- Registrar Matéria Prima')

        print('\n02- Ver o estoque de Matéria prima')
        
        print('\n03- Alterar matéria prima ')

        print('\n04- Deletar uma matéria prima')

        print('\n==================================')

        print('\n05- Adicionar itens ao catálogo')

        print('\n06- Vizualizar catálogo')

        print('\n07- Deletar item do catálogo')

        print('\n==================================')

        print('\n08- Cadastrar Funcionário')

        print('\n09- Mostrar Funcionários')

        print('\n10- Editar Funcionários')

        print('\n11- Deletar Funcionários')

        print('\n==================================')

        print('\n12- Caixa')

        print('\n13- Visualizar Histórico de compras')

        print('\n==================================')

        print('\n0- Voltar à tela de seleção de Usuário')

        print('\n==================================')


        opcao = input('\nSelecione uma opção: ')

        if opcao == '1':
            adicionar_informacao()
            while True:
                resp = input('\nAdicionar mais um produto? (y/n): ')

                if resp == 'y':
                    adicionar_informacao()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '2':
            visualizar_estoque()
            while True:
                resp = input('\nDeseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('\nOpção inválida!')


        elif opcao == '3':
            editar_estoque()
            while True:
                resp = input('\nEditar mais um item? (y/n): ')

                if resp == 'y':
                    editar_estoque()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '4':
            deletar_estoque()
            while True:
                resp = input('\nDeletar mais um item? (y/n): ')

                if resp == 'y':
                    deletar_estoque()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')
            
        elif opcao == '5':
            adicionar_produto()

            while True:
                resp = input('\nAdicionar mais um item ao catálogo? (y/n): ')

                if resp == 'y':
                    adicionar_produto()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '6':
            visualizar_cardapio()
            while True:
                resp = input('\nDeseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('\nOpção inválida!')
        
        elif opcao == '7':
            deletar_produto()
            while True:
                resp = input('\nDeletar mais um produto do catálogo? (y/n): ')

                if resp == 'y':
                    deletar_produto()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '8':
            registrar_funcionarios()
            while True:
                resp = input('\nDeseja Cadastrar mais um funcionário? (y/n): ')

                if resp == 'y':
                    registrar_funcionarios()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('Opção inválida!')

        elif opcao == '9':
            visualizar_funcionarios()
            while True:
                resp = input('Deseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('Opção inválida!')

        elif opcao == '10':
            editar_funcionarios()
            while True:
                resp = input('Deseja editar mais um funcionário? (y/n): ')

                if resp == 'y':
                    editar_funcionarios()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('Opção inválida!')

        elif opcao == '11':
            deletar_funcionario()
            while True:
                resp = input('Deseja deletar mais um funcionário? (y/n): ')

                if resp == 'y':
                    deletar_funcionario()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('Opção inválida!')
        elif opcao == '12':
            vender_produto()
            while True:
                resp = input('Deseja realizar mais uma venda? (y/n): ')

                if resp == 'y':
                    vender_produto()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('Opção inválida!')

        elif opcao == '13':
            visualizar_historico()
            while True:
                resp = input('Deseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('Opção inválida!')

        elif  opcao == '0':
            print('Programa encerrado')
            break

        else: 
            print('Opção inválida!')

def menuEstoquista():
     while True:
        print('\n=== Menu ===')

        print('\n01- Registrar Matéria Prima')

        print('\n02- Ver o estoque de Matéria Prima')

        print('\n03- Alterar matéria prima ')

        print('\n0- Voltar à tela de seleção de Usuário')
        
        print('\n=====================')

        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            adicionar_informacao()
            while True:
                resp = input('\nAdicionar mais um produto? (y/n): ')

                if resp == 'y':
                    adicionar_informacao()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '2':
            visualizar_estoque()
            while True:
                resp = input('\nDeseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('\nOpção inválida!')

        elif opcao == '3':
            editar_estoque()
            while True:
                resp = input('\nEditar mais um item? (y/n): ')

                if resp == 'y':
                    editar_estoque()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif  opcao == '0':
            print('\nPrograma encerrado')
            break
        else: 
            print('\nOpção inválida!')

def menuCaixaAtendente():
    while True: 
        print('\n=== Menu ===')

        print('\n1- Caixa')

        print('\n2- Histórico de compras')

        print('\n3- Adicionar itens ao catálogo')

        print('\n4- Mostrar catálogo')

        print('\n0- Voltar à tela de seleção de Usuário')

        print('\n=====================')
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            vender_produto()
            while True:
                resp = input('\nDeseja realizar mais uma venda? (y/n): ')

                if resp == 'y':
                    vender_produto()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')

        elif opcao == '2':
            visualizar_historico()
            while True:
                resp = input('\nDeseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('\nOpção inválida!')

        elif opcao == '3':
            adicionar_produto()
            while True:
                resp = input('\nAdicionar mais um item ao catálogo? (y/n): ')

                if resp == 'y':
                    adicionar_produto()

                elif resp == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                else:
                    print('\nOpção inválida!')
            
        elif opcao == '4':
            visualizar_cardapio()
            while True:
                resp = input('\nDeseja Retornar ao menu? (y): ')

                if resp == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
    
                else:
                    print('\nOpção inválida!')
            
        elif  opcao == '0':
            print('\nPrograma encerrado')
            break

        else: 
            print('\nOpção inválida!')

# Verificação de usuário

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n=== Tipo de usuário ===')

    print('\n1- Gerente')

    print('\n2- Estoquista')

    print('\n3- Caixa')

    print('\n0- Encerrar programa')

    print('\n=======================')

    usuario = input('Qual o seu tipo de usuário: ')

    if usuario == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        menuGerente()
            
    elif usuario == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        menuEstoquista()

    elif usuario == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        menuCaixaAtendente()
        
    elif usuario == '0':
        print('\nPrograma encerrado!')
        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nOpção inválida!')

