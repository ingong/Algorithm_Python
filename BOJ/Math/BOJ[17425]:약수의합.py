N = 7
D = [0 for _ in range(N+1)]
for i in range(2, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            D[i] += j

print(D)

MAX = 1000000
d = [1 for _ in range(MAX+1)]
s = [0 for _ in range(MAX+1)]
for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        d[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(s[n])
print('\n'.join(map(str,ans))+'\n')