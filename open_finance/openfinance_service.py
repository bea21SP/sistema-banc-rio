import json


def consultar_openfinance():

    cpf_busca = input("Digite CPF do cliente: ")

    bancos = [
        "banco1/database/clientes.json",
        "banco1/database/clientes.json",
    ]

    cliente_encontra = False

    saldo_total = 0
    divida_total = 0

    for banco in bancos:
        with open(banco, "r") as arquivo:

            clientes = json.load(arquivo)

        for cliente in clientes:

            if cliente["cpf"] == cpf_busca:

                print("\nDados Open Finance")

                print(f"""
Banco: {banco}

Nome: {cliente["nome"]}
CPF: {cliente["cpf"]}
Saldo: R$ {cliente["saldo"]:.2f}
Score: {cliente["score"]}
Dívida: {cliente["divida"]:.2f}
Negativado: {cliente["negativado"]}
""")
                saldo_total += cliente["saldo"]

                divida_total += cliente["divida"]

                cliente_encontra = True

    if cliente_encontra:
        print("\nResumo financeiro")

        print(f"Saldo total: R$ {saldo_total:.2f}")
        print(f"Dívida total: R$ {divida_total:.2f}")
        print(f"Patrimônio líquido: R$ {(saldo_total - divida_total):.2f}")

    else:

        print("Cliente não encontrado!")
