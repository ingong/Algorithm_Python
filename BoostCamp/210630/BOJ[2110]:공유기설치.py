import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    x = int(input())
    houses.append(x)
houses.sort()

start = 1
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    gap = (start + end) // 2
    point = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if point + gap <= houses[i]:
            count += 1
            point = houses[i]

    if count >= C:
        answer = gap
        start = gap + 1
    else:
        end = gap - 1

print(answer)



