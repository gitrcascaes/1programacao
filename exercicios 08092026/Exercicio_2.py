from datetime import datetime
print()
print(f"\033[31;43mCONTROLE DE ESTOQUE\033[0m");
print()

Produto = input("Digite o nome do produto: ")

Estoque = input (print "xxxxxxxxxxxxx: ")
if Estoque == "0":
    Outros = input("Para Outros, descreva seu problema com mais detalhes:");
print ()
print ()
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")


print()
if Estoque == "1":
   print ("\031[033mPRIORIDADE CRÍTICA!\031[0m")
elif Estoque == "2":
     print ("\031[033;035mPRIORIDADE ALTA!\031[0m")
elif Estoque =="3":
     print ("\033[031;035mPrioridade Média!\033[0m")
else:
    print("\035[031;037mPrioridade baixa!\035[0m")   