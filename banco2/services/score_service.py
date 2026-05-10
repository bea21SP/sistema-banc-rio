from utils.json_manager import carregar_clientes, salvar_clientes


def consultar_SCORE():
    
    cpf_busca = input("Digite o CPF do cliente: ")

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:

        if cliente["cpf"] == cpf_busca:

            score = cliente["score"]

            # REGRAS DO SCORE
            if cliente["saldo"] > 5000:
                score += 100

            elif cliente["saldo"] > 2000:
                score += 50

            elif cliente["saldo"] < 0:
                score -= 100

            cliente["score"] = score

            salvar_clientes(clientes)

            print("Score atualizado com sucesso!")

            print(f"Novo score: {cliente['score']}")

            cliente_encontrado = True
            break
    if not cliente_encontrado:
        print("Cliente não encontrado!")
