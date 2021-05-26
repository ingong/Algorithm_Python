N = int(input())
numList = list(map(int, input().split()))

for item in numList[::-1]:
    print(item, end=" ")

# 내 풀이
# for i in range(len(numList)-1, -1, -1):
#     print(numList[i], end=" ")