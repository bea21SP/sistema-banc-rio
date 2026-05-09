from utils.json_manager import carregar_clientes, salvar_clientes


def realizar_deposito():

    cpf_busca = input("Digite CPF do cliente: ").strip()

    clientes = carregar_clientes()

    cliente_encontrado = False

    for cliente in clientes:

        if cliente["cpf"] == cpf_busca:

            valor = float(input("Digite o valor do depósito: "))

            cliente["saldo"] += valor

            cliente["historico"].append(f"Depósito de R$ {valor:.2f}")

            salvar_clientes(clientes)

            print("Depósito realizado com sucesso!")

            print(f"Novo saldo: R$ {cliente['saldo']:.2f}")

            cliente_encontrado = True
            break

    if not cliente_encontrado:

        print("Cliente não encontrado!")


def realizar_saque():

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
                cliente["historico"].append(f"Saque de R$ {valor:.2f}")

                salvar_clientes(clientes)

                print("Saque realizado com sucesso!")
                print(f"Novo saldo: R$ {cliente['saldo']}")

                cliente_encontrado = True
                break

    if not cliente_encontrado:
        print("Cliente não encontrado!")


def realizar_PIX():
    cpf_origem = input("CPF de quem vai enviar: ")

    cpf_destino = input("CPF de quem vai receber: ")

    clientes = carregar_clientes()

    remetente = None
    destinatario = None


# Procurar clientes
    for cliente in clientes:
        if cliente["cpf"] == cpf_origem:
            remetente = cliente

        if cliente["cpf"] == cpf_destino:
            destinatario = cliente

        # Validar clientes
        if remetente is None:
            print("Remetente não encontrado!")

        elif destinatario is None:
            print("Destinatário não encontrado!")

        else:
            valor = float(input("Digite o valor do PIX: "))

            # Validar Saldo
            if valor > remetente["saldo"]:
                print("Saldo insuficiente!")

            else:
                remetente["saldo"] -= valor
                cliente["histórico"].append(f"PIX enviado de R$ {valor:.2f}")
                destinatario["saldo"] += valor
                destinatario["historico"].append(f"PIX recebido de R$ {valor:.2f}")

                salvar_clientes(clientes)

                print("PIX realizado com sucesso!")

                print(f"Novo saldo remetente: R$ {remetente['saldo']}")
                print(f"Novo saldo destinatário: R$ {destinatario['saldo']}")
