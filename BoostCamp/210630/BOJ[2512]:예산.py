N = int(input())
cities = list(map(int, input().split()))
budgets = int(input()) # 예산
start, end = min(cities), max(cities) # 시작 점, 끝 점
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for city in cities:
        if city < mid:
            total += city
        else:
            total += mid

    if total <= budgets:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1


print(answer)