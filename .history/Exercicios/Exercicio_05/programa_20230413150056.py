# Soma Impares

print("Digite dois números inteiros: ")

x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

for i in range(x + 1, y):
    soma = soma + i

print(f"A soma dos número ímpares no intervalo entre os números é  {soma}")