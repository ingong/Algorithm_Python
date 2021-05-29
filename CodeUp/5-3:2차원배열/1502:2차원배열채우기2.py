n = int(input())

for i in range(1, n+1):
    for j in range(0, n):
        print(i + n * j, end=" ")
        if j == n - 1:
            print()