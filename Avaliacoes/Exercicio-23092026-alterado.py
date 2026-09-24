livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Quantidade de livros")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
    
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        if len(livros) == 0:
            print("Nenhum livro cadastrado ainda.")
        else:
            for contador in livros:
                print("Título:", contador[0])
                print("Autor:", contador[1])
                print("-" * 30)

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        # Variável para controlar se achou o livro
        encontrado = False  

        for contador in livros:
            if contador[0] == pesquisa:
                print("\nLivro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
        
        if not encontrado:
            print("Nenhum livro correspondente foi encontrado.")

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        # Variável para controlar se excluiu o livro
        excluido = False  

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído com sucesso!")
                excluido = True
                # Para a repetição assim que remove o primeiro encontrado
                break  

        if not excluido:
            print("Nenhum livro correspondente foi encontrado para exclusão.")

    elif opcao == "5":
        
        print(f"\nQuantidade de livros cadastrados: {len(livros)}")

    elif opcao == "6":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")