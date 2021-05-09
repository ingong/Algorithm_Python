n, m = map(int, input().split(" "))
coins = [int(input()) for _ in range(n)]
count = 0
# for i in range(n, 0, -1):
#     print(i)
for i in reversed(range(n)):
    count += m // coins[i]
    m = m % coins[i]
print(count)

