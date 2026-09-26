print()
print ("-" * 10, "CADASTRO DE COLABORADORES", "-" * 10)
colaboradores = []
while True:
    def imprimi_menu ():
     print ("1 - CADASTRAR COLABORADOR(a)\n2 - LISTAR COLABORADORES\n3 - EXCLUIR COLABORADORES")
    imprimi_menu()
    item = int (input ("QUAL AÇÃO VOCÊ QUER EXECUTAR? "))
    if item == 1:
        nome = input("NOME: ")
        departamento = input ("DEPARTAMENTO: ")
        cargo = input ("CARGO: ")
        colaboradores.append([nome,departamento,cargo])
        print()
        print("-" *10, "COLABORADOR CADASTRADO COM SUCESSO", "-"*10)
    if item == 2:
        print("-" *10, "LISTA DE COLABORADORES CADASTRADOS: ", "-"*10)
        if len(colaboradores) == 0:
           print("Não há colaboradores cadastrados.")
    else:
       for contador in colaboradores:
          print("nome:", contador[0])
          print("departamento:", contador[1])
          print("cargo:", contador[2])