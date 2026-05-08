# Criando uma lista, colocando clientes nela e salvando no json.
from utils.json_manager import carregar_clientes, salvar_clientes


while True: # “repita infinitamente”

    #Opções disponíveis para o cliente
    print("\n===== BANCO OPEN FINANCE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar Cliente")
    print("4 - Depositar")
    print("5 - Sacar")
    print("6 - Sair")

    #Guarda o que o usuário escolheu.
    opcao = input("Escolha uma opção: ")

    # CADASTRAR CLIENTE
    if opcao == "1":

        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        saldo = float(input("Digite o saldo: "))
        score = int(input("Digite o score: "))

        novo_cliente = {
            "nome": nome,
            "cpf": cpf,
            "saldo": saldo,
            "score": score
        }

        clientes = carregar_clientes()

        cpf_existe = False # ainda não encontrei o CPF

        # Percorre todos os clientes
        for cliente in clientes:

            if cliente["cpf"] == cpf: #compara CPF no json
                cpf_existe = True
                break


        if cpf_existe:
            print("CPF já cadastrado!")

        else:
            clientes.append(novo_cliente)

            salvar_clientes(clientes)

            print("Cliente cadastrado com sucesso!")

    # LISTAR CLIENTES
    elif opcao == "2":

        clientes = carregar_clientes()

        print("\n===== CLIENTES =====")

        # Pegando cada cliente cadastrado
        for cliente in clientes:
            print(f"""
    Nome: {cliente["nome"]}
    CPF: {cliente["cpf"]}
    Saldo: R$ {cliente["saldo"]}
    Score: {cliente["score"]}
    """)
            
    # Buscar Cliente
    elif opcao == "3":

        cpf_busca = input("Digite o CPF do cliente: ")

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:

                print("\n CLIENTE ENCONTRADO")
                print(f"""
Nome: {cliente["nome"]}
CPF: {cliente["cpf"]}
Saldo: R$ {cliente["saldo"]}
Score: {cliente["score"]}
""")
                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")

    # Depósito
    elif opcao == "4":

        cpf_busca = input("Digite o CPF do cliente: ")

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:

                valor = float(input("Digite o valor do deposito: "))

                cliente["saldo"] += valor
                salvar_clientes(clientes)

                print("Depósito realizado com sucesso!")

                print(f"Novo saldo: R$ {cliente['saldo']}")

                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")    

    # Sacar
    elif opcao == "5":
        cpf_busca = input("Digite o CPF do cliente: ")

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:

                valor = float(input("Digite o valor do saque: "))

                if valor > cliente["saldo"]:
                    print("Saldo insuficiente!")
                else:
                    cliente["saldo"] -= valor    

                    salvar_clientes(clientes)

                    print("Saque realizado com sucesso!")
                    print(f"Novo saldo: R$ {cliente['saldo']}")

                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")    
        


    # SAIR
    elif opcao == "6":
        print("Encerrando sistema...")
        break

    

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida!")