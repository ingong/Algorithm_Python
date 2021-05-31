N = int(input())

A = list(map(int, input().split()))
D = [0 for _ in range(N)]

for i in range(N):
    D[i] = A[i]
    for j in range(i):
        if A[j] <= A[i]:
            D[i] = max(D[i], D[j]+A[i])

print(max(D))