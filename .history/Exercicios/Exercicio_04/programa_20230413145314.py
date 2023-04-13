# Problema crescente

a = int(input("Digite um valor inteiro qualquer: "))
b = int(input("Digite um valor inteiro qualquer: "))

while a !=b:
    if (a < b):
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    input("Digite outros dois números inteiros ou dois números iguais para parar: ")
    a = int(input())
    b = int(input())
print("FIM DA EXECUÇÃO")