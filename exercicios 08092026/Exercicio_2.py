# Consulta de produtos em estoque (ficticio)
print()
print()
produto = input ("Nome do produto:")
quantidade = int(input("Quantidade disponível:"))
if quantidade == 0:
   status = print ("Estoque zerado")
elif 1 <= quantidade <=5:
   status = print("Estoque crítico")
elif 6 <= quantidade <=20:
   status = print ("Estoque baixo")
else:
   status = print ("Estoque Normal!")
print()
print()
