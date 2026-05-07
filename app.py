# Criando uma lista, colocando clientes nela e salvando no json.
from utils.json_manager import carregar_clientes, salvar_clientes


while True: # “repita infinitamente”

    #Opções disponíveis para o cliente
    print("\n===== BANCO OPEN FINANCE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

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

    # SAIR
    elif opcao == "3":
        print("Encerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida!")