# Diagonal Negativos de Matriz

N = int(input("Qual a ordem da matriz? ")) # A ordem define mesmo número de linhas x colunas

mat = [[0 for x in range(N)] for x in range(N)]  # Lista de Listas

for i in range(0,N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("MATRIZ DIGITADA:")
for i in range(0, N):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")
    print()


print("DIAGONAL PRINCIPAL")
for i in range(0, N):
    print(f"{mat[i][i]} ", end="")    
print()

print("QUANTIDADE DE NÚMEROS NEGATIVOS:")
cont = 0
for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] < 0:
             cont = cont + 1       

print("")
  