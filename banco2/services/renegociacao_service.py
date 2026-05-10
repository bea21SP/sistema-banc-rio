from utils.json_manager import carregar_clientes, salvar_clientes


def pagar_divida():

    cpf_busca = input("Digite CPF do cliente: ")

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:
        if cliente["cpf"] == cpf_busca:

            # Verificar se tem dívida
            if cliente["divida"] <= 0:

                print("Cliente não possui dívidas.")

            else:
                print(f"Dívida atual: R$ {cliente['divida']:.2f}")

                valor_pagamento = float(input("Digite o valor do pagamento: "))

                # Não pode pagar mais que a dívida
                if valor_pagamento > cliente["divida"]:

                    print("Valor maior que a dívida!")

                elif valor_pagamento > cliente["saldo"]:

                    print("Saldo insuficiente!")

                else:
                    cliente["saldo"] -= valor_pagamento
                    cliente["divida"] -= valor_pagamento
                    cliente["historico"].append(
                        f"Pagamento de dívida de R$ {valor_pagamento:.2f}"
                    )

                    salvar_clientes(clientes)

                    print("Pagamento realizado com sucesso!")

                    print(f"Novo saldo: R$ {cliente["saldo"]:.2f}")
                    print(f"Dívida restante: R$ {cliente["divida"]:.2f}")

                    cliente_encontrado = True
                    break

    if not cliente_encontrado:
        print("Cliente não entrado!")


def verificar_negativacao():

    cpf_busca = input("Digite CPF do cliente: ").strip()

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:
        if cliente["cpf"] == cpf_busca:

            # Regra de negativação
            if cliente["divida"] > 10000:

                cliente["negativado"] = True

                cliente["score"] -= 200

                salvar_clientes(clientes)

                print("Cliente negativado!")

                print(f"Novo score: {cliente['score']}")

            else:
                print("Cliente não possui dívida suficiente para negativação.")

                cliente_encontrado = True
                break

    if not cliente_encontrado:
        print("Cliente não encontrado!")


def renegociar_divida():
    cpf_busca = input("Digite CPF do cliente: ").strip()

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:

        if cliente["negativado"] and cliente["divida"] > 0:

            print(f"Dívida atual: R$ {cliente['divida']:.2f}")

            desconto = cliente["divida"] * 0.20

            cliente["divida"] -= desconto

            cliente["score"] += 100

            cliente["negativado"] = False
            cliente["historico"].append("Renegociação realizada")

            salvar_clientes(clientes)

            print("Renegociação realizada com sucesso!")

            print(f"Desconto aplicado: R$ {desconto:.2f}")
            print(f"Nova dívida: R$ {cliente['divida']:.2f}")
            print(f"Novo score: R$ {cliente['score']:.2f}")

        else:
            print("Cliente não está negativado.")

            cliente_encontrado = True
            break

    if not cliente_encontrado:
        print("Cliente não encontrado!")
