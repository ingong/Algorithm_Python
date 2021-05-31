# 모든 작게 만드는 방법을 다 찾았는지
N = int(input())
D = [0 for _ in range(N+1)]

D[0] = 1
for i in range(2, N+1, 2):
    D[i] = D[i-2] * 3
    for j in range(i-4, -1, -2):
        D[i] += D[j] * 2

print(D[N])
