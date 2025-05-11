n = input("Qual variável você deseja aprender (String, Boolean, Float, Integer.)? ").lower()

if n == "string":
  print("Uma string é uma sequência de caracteres (letras, números, símbolos, etc.) utilizada para representar texto")
elif n == "boolean":
  print("um booleano (ou valor booleano) é um tipo de dado que pode ter apenas dois valores possíveis: verdadeiro (true) ou falso (false). É uma forma de representar estados binários, como ligado/desligado, sim/não, ou 1/0.")
elif n == "float":
  print("refere-se a um tipo de dado numérico que representa números com casas decimais. É usado para representar valores fracionários ou números grandes/pequenos que não podem ser representados com precisão por números inteiros.")
elif n == "integer":
  print("em programação e matemática refere-se a um número inteiro, ou seja, um número sem parte fracionária ou decimal.")
else:
  print("Erro, Tente Novamente!")