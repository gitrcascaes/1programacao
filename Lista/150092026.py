#APRENDENDO A CRIAR LISTAS - BANCO DE DADOS
#"\033[31;43m---LIBRARY SYSTEM---\033[0m"
print()
while True:
    print()
    print(f"\033[33;34m------INTEGRANTES DA FAMILIA-----\033[0m")
    Familia_Rosana = ['Rosana','Niky', 'Nicolle','Heloisa']
    Familia_Vasconcelos = ["França", "Francisco", "Rose", "Jane","Lane","Janne", "Cris", "Niki"]
    Familia_Rosa = ["Rosa", "Branco", "Rosana", "Roseane","Rosangela", "Ewerton", "Emerson"]
    print ("As Familia são: ")
    print ("1 - Familia Rosana")
    print ("2 - Familia vasconcelos")
    print ("3 - Familia Rosa")
    print ("0 - Sair do Programa")
    item = input("Digite qual família você deseja conhecer os integrantes?")
    if item =="1":

#if opcao == "1":
        print("Os integrantes da Família da Rosana são:")
        for integrante in Familia_Rosana:
            print(f"- {integrante}")
            
    elif opcao == "2":
        print("Os integrantes da Família Vasconcelos são:")
        for integrante in Familia_Vasconcelos:
            print(f"- {integrante}")
            
    elif opcao == "3":
        print("Os integrantes da Família Rosa são:")
        for integrante in Familia_Rosa:
            print(f"- {integrante}")
            
    elif opcao == "0":
        print("\033[31mSaindo do sistema...\033[0m")
        break  # Interrompe o laço e fecha o programa
        
    else:
        print("\033[31mOpção inválida! Tente novamente.\033[0m")
        
    # Mensagem visual antes de reiniciar o loop
    print(f"\n\033[31m ******* CONSULTAR PRÓXIMA FAMÍLIA ******* \33[0m")
   
#familias = (f"\033[31m *******CONSULTAR PROXÍMA FAMÍLIA***** \33[0m")
