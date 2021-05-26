N = int(input())
numList = list(map(int, input().split()))

# 조금 더 나은 풀이
for i in range(N):
    for j in range(N):
        print(numList[i+j-N], end=" ")
    print()

# 내 처음 풀이
# newList = numList * N
# for i in range(N):
#     for j in range(i, N+i):
#         print(newList[j], end=" ")
#     print()


