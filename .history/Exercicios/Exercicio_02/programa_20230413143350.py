import math
# Problema idades:

print("Dados da Primeira Pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("idade: "))

print("Dados da Segunda Pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("idade: "))

media = (idade1 + idade2) / 2.0

print(f"{nome1} tem {idade1} anos e {nome2} tem {idade2} anos e a média de idades é {media:.2}")
