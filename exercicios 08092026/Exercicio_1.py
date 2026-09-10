from datetime import datetime
print()
print(f"\033[31;43mDados do usuário\033[0m");
print()
print(f"Prezado(a) usuário(a), seja bem vindo ao chamado Help Desk!");
print()
print(f"Preencha o formulário a seguir para registro da sua ocorrência!");
nome = input("Digite seu nome: ");
Departamento = input("Digite seu departamento: ")
while True:
    Contato = input("Digite seu contato: ");
    if Contato.isdigit():
       break
else:
    print("Digite apenas números,sem espaço e letras, ou outros caracteres")
  
print()
print(f"\033[31;43mDados do equipamento:\033[0m");
Equipamento = input("Qual a marca : ");
modelo = input("Qual Modelo: ");
print()
print(f"\033[31;43mIndique qual número corresponde ao problema que a sua máquina está apresentando:\033[0m");
print("1-Indisponibilidade total do sistema:", "2-Sistema funcionando, mas com lentidão e ou erros:", "3-Problemas que não impede o trabalho", "4-Outros problemas", sep="\n")
print()
problema = input("Escolha o número do problema: ")
if problema == "4":
    Outros = input("Para Outros, descreva seu problema com mais detalhes:");
print ()
print ()
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
print(f"Chamado registrado com sucesso em: {data_atual}")
print()
print(f"\033[31;43mCONTROLE HELP DESK:\033[0m");
print()
print(f"\033[31;43mPrioridade da ação:\033[0m");
print()
if problema == "1":
   print ("\031[033mPRIORIDADE CRÍTICA!\031[0m")
elif problema == "2":
     print ("\031[033;035mPRIORIDADE ALTA!\031[0m")
elif problema =="3":
     print ("\033[031;035mPrioridade Média!\033[0m")
else:
    print("\035[031;037mPrioridade baixa!\035[0m")   