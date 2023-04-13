# Diagonal Negativos de Matriz

N = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(N)] for x in range(N)]  # Lista de Listas

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))