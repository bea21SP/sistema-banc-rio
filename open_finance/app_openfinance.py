from openfinance_service import consultar_openfinance

while True:
    
    print("\nOpen Finance")
    print("1 - Consultar cliente")
    print("2 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        
        consultar_openfinance()
        
    elif opcao == "0":
        break    