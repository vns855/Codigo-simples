import random
na = random.randint (1,10)

contador = 0
while True:
  e = int(input("Escolha um número de 1 a 10: "))
  contador += 1 
  if e == na:
    break
  
print(f"O número que foi advinhado era {na}, e você precisou {contador} tentativa(s)!")