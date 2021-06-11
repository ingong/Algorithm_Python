N = 5
liquids = [-2, 4, -99, -1, 98]
abs_liquids = sorted(liquids, key=abs)
print(abs_liquids)
minV = 2000000000
ans = (0, 0)

for i in range(1, N):
    if abs(abs_liquids[i] + abs_liquids[i-1]) < minV:
        minV = abs(abs_liquids[i] + abs_liquids[i-1])
        answer = (abs_liquids[i], abs_liquids[i-1])

print(" ".join(map(str, sorted(answer))))