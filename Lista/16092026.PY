#APRENDENDO A CRIAR LISTAS - BANCO DE DADOS
familia1 = ['Rosana','Niky', 'Nicolle','Heloisa']
familia2 = ["França", "Francisco", "Rose", "Jane","Lane","Janne", "Cris", "Niki"]
familia3 = ["Rosa", "Branco", "Rosana", "Roseane","Rosangela", "Ewerton", "Emerson"]
print()
print()
item =1
while item!= 0:
      print(f"\033[33;34m------INTEGRANTES DA FAMILIA-----\033[0m")
      print("1 - FAMILIA ROSANA")
      print("2 - FAMILIA VASCONCELOS")
      print("3 - FAMILIA ROSA")
      print("0 - SAIR DO PROGRAMA")
      item = int(input("Digite o nº da família que você deseja conhecer os integrantes? "))
      if item ==1: 
         print(f"\033[33;34m------Esse são os integrantes da família escolhida:-----\033[0m")
         for  contador in familia1:
          print (contador)
      elif item ==2:
           print(f"\033[33;34m------Esse são os integrantes da família escolhida:-----\033[0m")
           for contador in familia2:
            print (contador)
      elif item ==3:
           print(f"\033[33;34m------Esse são os integrantes da família escolhida:-----\033[0m")
           for contador in familia3:
            print (contador)
      elif item ==0:
           print (f"\033[33;34m------Você escolheu sair do programa-----\033[0m!")
      else:
          print ("Informação inválida! Digite apenas números de 0 a 3")
print()
print()


