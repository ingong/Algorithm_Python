n = int(input())
board = [[i + j * n for i in range(1, n+1)] for j in range(0, n)]

# board = [[0 for i in range(COLUM)] for j in range(ROW)]

for i in range(1, n**2 + 1):
    print(i, end=' ')
    if i % n == 0:
        print()
