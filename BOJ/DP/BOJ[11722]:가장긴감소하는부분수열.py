# 로직 설계
# 코드 구현
# 틀렸던 부분 : 이전 까지의 D[i] 와 새로운 D[j] + 1 간의 값을 비교해서 최대값을 찾아야한다
N = int(input())
A = list(map(int, input().split()))
D = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            D[i] = max(D[j] + 1, D[i])

print(max(D))