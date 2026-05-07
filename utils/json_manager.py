import json

def carregar_clientes():
    with open("database/clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

    return clientes


def salvar_clientes(clientes):
    with open("database/clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)