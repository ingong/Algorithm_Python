from itertools import combinations, permutations
N, S = map(int, input().split())
numList = list(map(int, input().split()))
numList = [*map(int, input().split())]

result = []
answer = 0

for j in range(1, N+1):
    for i in permutations(numList, j):
        if sum(i) == S:
            result.append(i)
            answer += 1

print(answer)
print(result)