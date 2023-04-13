# Problema crescente

a = int(input("Digite um valor inteiro qualquer: "))
b = int(input("Digite um valor inteiro qualquer: "))

while a !=b:
    if (a < b):
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    a = int(input("Digite outro valor inteiro qualquer ou : "))
    b = int(input("Digite outro valor inteiro qualquer: "))
print("FIM DA EXECUÇÃO")