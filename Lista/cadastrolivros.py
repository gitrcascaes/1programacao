
# SISTEMA PARA BIBLIOTECA

lista_codigos = []
lista_titulos = []
lista_autores = []
lista_anos = []

opcao = 1

while opcao != 4:
    print()
    print(f"\033[31;43m---LIBRARY SYSTEM---\033[0m")
    print()
    print("MENU DE OPÇÕES:")
    print()
    print("1 = CADASTRAR LIVRO (CREATE)")
    print("2 = LISTAR LIVROS   (READ)")
    print("3 = EXCLUIR LIVRO   (DELETE)")
    print("4 = SAIR")
    print()
    
    opcao = int(input("Escolha uma opção: "))
    
    # 1. CREATE (Cadastrar)
    if opcao == 1:
        print("\nVAMOS CADASTRAR O LIVRO!")
        quantidade_livro = int(input("QUANTOS LIVROS DESEJA CADASTRAR: "))
        
        for i in range(quantidade_livro):
            print(f"\n--- Cadastro do {i+1}º livro ---")
            
            codigo = int(input("Código do livro (apenas números): "))
            titulo_livro = str(input("Título do livro: "))
            autor = str(input("Nome do Autor: "))
            ano_publ = int(input("Ano de publicação: "))
            
            # Validação simples: se algum campo de texto estiver vazio
            if titulo_livro == "" or autor == "":
                print("Erro: Preencha todos os campos corretamente!")
            else:
                # Adiciona os dados nas listas correspondentes
                lista_codigos.append(codigo)
                lista_titulos.append(titulo_livro)
                lista_autores.append(autor)
                lista_anos.append(ano_publ)
                print("Livro cadastrado com sucesso!")
                
    # 2. READ (Listar/Ver)
    else:
        if opcao == 2:
            print("\n--- LIVROS CADASTRADOS ---")
            # Se a lista estiver vazia
            if len(lista_codigos) == 0:
                print("Nenhum livro cadastrado ainda.")
            else:
                # O for percorre as posições das listas
                for i in range(len(lista_codigos)):
                    print(f"Posição: {i} | Código: {lista_codigos[i]} | Título: {lista_titulos[i]} | Autor: {lista_autores[i]} | Ano: {lista_anos[i]}")
                    
        # 3. DELETE (Excluir)
        else:
            if opcao == 3:
                print("\n--- EXCLUIR LIVRO ---")
                if len(lista_codigos) == 0:
                    print("Nenhum livro para excluir.")
                else:
                    codigo_excluir = int(input("Digite o código do livro que deseja excluir: "))
                    
                    # Variável para saber se encontramos o livro
                    achou = False
                    
                    for i in range(len(lista_codigos)):
                        if lista_codigos[i] == codigo_excluir:
                            # Remove o item de todas as listas usando a posição 'i'
                            lista_codigos.pop(i)
                            lista_titulos.pop(i)
                            lista_autores.pop(i)
                            lista_anos.pop(i)
                            print("Livro excluído com sucesso!")
                            achou = True
                            break # Para o for, pois já encontrou
                            
                    if achou == False:
                        print("Código de livro não encontrado.")
                        
            # 4. SAIR
            else:
                if opcao == 4:
                    print()
                    print(f"\033[31;43m---Até a próxima!---\033[0m")
                    print()
                else:
                    print("Opção inválida! Tente novamente.")