from utils.json_manager import salvar_clientes

clientes = [
    {
        "nome": "Beatriz",
        "cpf": "123",
        "saldo": 1000,
        "score": 800
    }
]

salvar_clientes(clientes)

print("Clientes salvos com sucesso!")