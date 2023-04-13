# Problema crescente

a = int(input("Digite um valor inteiro qualquer: "))
b = int(input("Digite um valor inteiro qualquer: "))

while a !=b:
    if (a < b):
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    print("Digite outros dois números inteiros ou dois números iguais para encerrar: ")
    a = int(input())
    b = int(input())
print("FIM DA EXECUÇÃO")