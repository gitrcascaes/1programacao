#SISTEMA PARA BIBLIOTECA
print()
print (f"\033[31;43m---LIBRARY SYSTEM---\033[0m");
print()
print("MENU DE OPÇÕES:")
print()
print ("CADASTRAR LIVROS =     1\nCADASTRAR ALUNOS =     2\nREALIZAR EMPRESTIMO =  3\nSAIR =                 4")
print()
numero = int(input("DIGITE O NUMERO CORRESPONDENTE A AÇÃO DESEJADA: "))
if numero == 1:
   print ("VAMOS CADASTRAR O LIVRO!")
   quantidade_livro = int(input("QUANTOS LIVROS DESEJA CADASTRAR: "))
   for i in range(quantidade_livro):
     print(f"\n--- Cadastro do {i+1}º livro ---")
     codigo = int(input("Código do livro: "))
     titulo_livro = str(input("Título do livro: "))
     autor = str(input("Nome do Autor: "))
     ano_publ = int(input("Ano de publicação: "))
     if titulo_livro == "":
        print("Erro: Preencha os dados do título!")
     if autor == "":
        print ("Erro: Preencha os dados do autor")
     if ano_publ == "":
        print ("Erro: Preencha o ano de publicação com quatro dígitos")
     disp_livro = input("Quantidade disponível: ")
     print()
     print("Livro cadastrado com sucesso!")
if numero == 2:
   quantidade_aluno = int(input("QUANTOS ALUNOS DESEJA CADASTRAR: "))
   for i in range(quantidade_aluno):
     print(f"\n--- Cadastro do {i+1}º Aluno ---")
     matricula = input("Matrícula: ")
     nome_aluno = str (input("Nome do aluno: "))
     turma = input("Turma: ")
     if matricula == "":
        print ("Preencha o numero da matricula ")
     if nome_aluno == "":
        print (" Preencha o nome do Aluno ")
     if turma == "":
        print (" Preencha turma")
        print()
     print ("Aluno cadastrado com sucesso!!")
if numero == 3:  
   codigo_livro = input("Código do livro: ")
   matricula_aluno = input("Matrícula do aluno: ")
   print()
   print("Empréstimo realizado com sucesso!")
else:
    print()
    print(f"\033[31;43m---Até a proxíma!---\033[0m")
    print()
    print()