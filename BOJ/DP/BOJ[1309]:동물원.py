N = int(input())
D = [[0,0,0], [1,1,1]] + [[0, 0, 0] for _ in range(N-1)]
# d = [[0]*3 for _ in range(N+1)]
# print(d)
for i in range(2, N+1):
    D[i][0] = D[i-1][0] + D[i-1][1] + D[i-1][2]
    D[i][1] = D[i-1][0] + D[i-1][2]
    D[i][2] = D[i-1][0] + D[i-1][1]
    for j in range(3):
        D[i][j] %= 9901
print(sum(D[N]) % 9901)


# D = [[0, 0, 0] for _ in range(N+1)]
# D[0][0] = 1
# for i in range(1, n+1)
