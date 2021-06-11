M, N = 3, 16
prime = set(range(M, N+1))
for i in range(2, N+1):
    prime -= set(range(i**2, N+1, i))

for number in prime:
    print(number)