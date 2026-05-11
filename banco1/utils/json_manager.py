import json

def carregar_clientes(): #abre o json e transforma os dados em python
    try: #tratativa de erro se o json estiver vazio

        with open("banco1/database/clientes.json", "r", encoding="utf-8") as arquivo:
            clientes = json.load(arquivo)

        return clientes
    except:

        return []

def salvar_clientes(clientes): #transforma uma lista Python em json e salva o arquivo.
    with open("banco1/database/clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, 
                  arquivo, 
                  indent=4,
                  ensure_ascii=False
                  )