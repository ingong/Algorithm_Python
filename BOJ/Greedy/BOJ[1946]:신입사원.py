import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append(a, b)

    arr.sort()
    min_Val = 10e9
    cnt = 0
    for (x, y) in arr:
        if min_Val > y:
            minVal = y
            cnt += 1
    print(cnt)