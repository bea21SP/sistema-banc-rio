# Criando uma lista, colocando clientes nela e salvando no json.
from utils.json_manager import carregar_clientes, salvar_clientes
from services.cliente_service import cadastrar_cliente
from services.cliente_service import listar_clientes
from services.cliente_service import buscar_cliente
from services.cliente_service import realizar_deposito
from services.cliente_service import realizar_saque
from services.emprestimo_service import realizar_emprestimo
from services.renegociacao_service import pagar_divida
from services.renegociacao_service import verificar_negativacao
from services.renegociacao_service import renegociar_divida
from services.score_service import consultar_SCORE


while True: # “repita infinitamente”

    #Opções disponíveis para o cliente
    print("\n===== BANCO OPEN FINANCE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar Cliente")
    print("4 - Depositar")
    print("5 - Sacar")
    print("6 - PIX")
    print("7 - SCORE")
    print("8 - Solicitar empréstimo")
    print("9 - Pagar dívida")
    print("10 - Verificar negativação")
    print("11 - Renegociar dívida")
    print("12 - Ver histórico")
    print("13 - Sair")

    #Guarda o que o usuário escolheu.
    opcao = input("Escolha uma opção: ")

    # CADASTRAR CLIENTE
    if opcao == "1":

        cadastrar_cliente()
        
    elif opcao == "2":
            
        listar_clientes()   

    elif opcao == "3":
        
        buscar_cliente()
    
    elif opcao == "4":
        
        realizar_deposito()
        
    elif opcao == "5":
        
        realizar_saque(), 
        
    elif opcao == "6":
        
        realizar_PIX()  
        
    elif opcao == "7":
        
        consultar_SCORE()      
        
    elif opcao == "8":
        realizar_emprestimo()    
        
    elif opcao == "9":
        
        pagar_divida()    
        
    elif opcao == "10":
        
        verificar_negativacao()
        
    elif opcao == "11":
        renegociar_divida()   
        

    elif opcao == "12":
        consultar_historico()    
        
    elif opcao == "13":
        print("Encerrando sistema...")
        break
    
    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida!")    
        
"""
    # LISTAR CLIENTES
    elif opcao == "2":

        clientes = carregar_clientes()

        print("\n===== CLIENTES =====")

        # Pegando cada cliente cadastrado
        for cliente in clientes:
            print(f"""
#Nome: {cliente["nome"]}
#CPF: {cliente["cpf"]}
#Saldo: R$ {cliente["saldo"]}
#Score: {cliente["score"]}
#""")
"""          
    # Buscar Cliente
    elif opcao == "3":

        cpf_busca = input("Digite o CPF do cliente: ")

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:

                print("\n CLIENTE ENCONTRADO")
                print(f"""
#Nome: {cliente["nome"]}
#CPF: {cliente["cpf"]}
#Saldo: R$ {cliente["saldo"]}
#Score: {cliente["score"]}
""")
                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")


        cpf_busca = input("Digite o CPF do cliente: ")

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:

                valor = float(input("Digite o valor do deposito: "))

                cliente["saldo"] += valor
                cliente["historico"].append(f"Depósito de R$ {valor:.2f}")
                salvar_clientes(clientes)

                print("Depósito realizado com sucesso!")

                print(f"Novo saldo: R$ {cliente['saldo']}")

                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")    

    elif opcao == "5":
        
        realizar_saque()


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
     
    # PIX
    elif opcao == "6":
        realizar_PIX(),

        cpf_origem = input("CPF de quem vai enviar: ")
        cpf_destino = input("CPF de quem vai receber: ")

        clientes = carregar_clientes()

        remetente = None
        destinatario = None

        #Procurar clientes
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

            #Validar Saldo
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

    # SCORE
    elif opcao == "7":
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

    # Empréstimo
    elif opcao == "8":
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

    # Pagar dívida
    elif opcao == "9":
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
                        cliente["historico"].append(f"Pagamento de dívida de R$ {valor_pagamento:.2f}")

                        salvar_clientes(clientes)

                        print("Pagamento realizado com sucesso!")     

                        print(f"Novo saldo: R$ {cliente["saldo"]:.2f}")    
                        print(f"Dívida restante: R$ {cliente["divida"]:.2f}")   

                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não entrado!")

    # Verificar negativação
    elif opcao == "10":
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

    # Renegociar dívida
    elif opcao == "11":
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

    # Ver histórco
    elif opcao == "12":
        cpf_busca = input("Digite o CPF do cliente: ").strip()

        clientes = carregar_clientes()

        cliente_encontrado = False

        for cliente in clientes:

            if cliente["cpf"] == cpf_busca:

                print("\nHISTÓRICO FINANCEIRO")

                if len(cliente["historico"]) == 0:
                    print("Nenhuma movimentação encontrada.")

                else:
                    for movimentacao in cliente["historico"]:

                        print(f"- {movimentacao}")  
                        
                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Cliente não encontrado!")

    # SAIR
    elif opcao == "13":
        print("Encerrando sistema...")
        break

    

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida!")
        
"""       