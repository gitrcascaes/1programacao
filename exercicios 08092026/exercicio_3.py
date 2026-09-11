# Velocidade da internet
print()
print()
Cliente = input ("Nome do Cliente:")
velocidade = int(input("Velocidade contratada:"))
if velocidade <=50:
   status = print ("Plano básico!")
elif 50 <= velocidade <=199:
   status = print ("plano intermediário!")
elif 200 <= velocidade <=499:
   status = print ("Plano avançado!")
else:
   status = print ("parabéns seu plano é ultra!")
print()
print()

print ("Seu plano é:", status)
print()
