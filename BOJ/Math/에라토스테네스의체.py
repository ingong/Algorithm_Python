Max = 1000000
check = [0 for _ in range(Max+1)]

for i in range(2, Max+1):
    if not check[i]:
        j = i + i
        while j <= Max:
            check[i] = True
            j += i


n, m = map(int, input().split())
for i in range(n, m+1):
    if check[i] == False:
        print(i)