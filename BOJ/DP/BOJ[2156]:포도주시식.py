N = int(input())
Wines = [0] * (N+1)
D = [0] * (N+1)
for i in range(1, N+1):
    Wines[i] = int(input())

D[1] = Wines[1]
if N >= 2:
    D[2] = Wines[1] + Wines[2]

for i in range(3, N+1):
    D[i] = max(D[i-1], D[i-2] + Wines[i], D[i-3] + Wines[i-1] + Wines[i])

print(D[N])