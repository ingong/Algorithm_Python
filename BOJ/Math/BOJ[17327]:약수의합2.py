# while True:
# test_case = int(input())
# for _ in range(test_case):
N = int(input())
g = 0
for i in range(1, N+1):
    val = (N // i) * i
    g += val
print(g)
