print()
def menu ():
    print ("1 - Arroz\n2 - Açucar\n3 - café\n4 - Leite\n5 - Sair")
print ("--------COTAÇÃO DE PRODUTOS------")
while True:
    menu()
    item = int(input("Qual o nº do item que você deseja consultar? "))
    preco = 0.0
    if item == 1:
        print("Arroz - R$ Un: 5,00 ")
        preco = 5.00
    elif item == 2:
        print("Açucar - R$ Un: 3,00")
        preco = 3.00
    elif item == 3:
        print("café - R$ Un: 19,00 ")
        preco = 19.00
    elif item == 4:
        print("Leite - R$ Un: 18,00 ")
        preco = 18.00
    elif item == 5:
        print ("Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue
    if item in [1,2,3,4]:
        quantidade = int(input ("Quantidade desejada: "))
        valor = preco * quantidade
        print (f"Valor total da cotação: R$ {valor:.2f}")
print()