# Soma Impares

print("Digite dois números inteiros: ")

x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x + 1, y):
    if i % 2 != 0:
        soma = soma + i

print(f"A soma dos número ímpares no intervalo entre os números {x} e é  {soma}")