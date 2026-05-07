import json

def carregar_clientes(): #abre o json e transforma os dados em python
    with open("database/clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

    return clientes


def salvar_clientes(clientes): #transforma uma lista Python em json e salva o arquivo.
    with open("database/clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)