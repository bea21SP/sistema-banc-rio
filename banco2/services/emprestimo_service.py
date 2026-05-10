from utils.json_manager import carregar_clientes, salvar_clientes

def realizar_emprestimo():
    cpf_busca = input("Digite CPF do cliente: ")

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:

        if cliente["cpf"] == cpf_busca:

            valor = float(input("Digite o valor do empréstimo: "))
            parcelas = int(input("Digite a quantidade de parcelas: "))

            parcela = valor / parcelas

            limite_parcela = cliente["renda_mensal"] * 0.30

            score = cliente["score"]

                # Análise de crédito
            if score >= 700 and parcela <= limite_parcela:

                cliente["saldo"] += valor
                cliente["divida"] += valor
                cliente["historico"].append(f"Empréstimo aprovado de R$ {valor:.2f}")

                salvar_clientes(clientes)

                print("Empréstimo aprovado!")
                print(f"Valor da parcela: R$ {parcela:.2f}")
                print(f"Limite permitido: R$ {limite_parcela:.2f}")

            elif score >= 500 and parcela <= limite_parcela:

                print("Em análise manual.")

            else:

                print("Empréstimo negado!")

                cliente_encontrado = True
                break    

    if not cliente_encontrado:
        print("Cliente não encontrado!")            
