N = 5
liquids = [-2, 4, -99, -1, 98]
liquids.sort()
left = 0
right = N - 1
ans = (0, 0)
minVal = 2000000000

while left <= right:
    total = liquids[left] + liquids[right]
    if abs(total) < minVal:
        minVal = abs(total)
        ans = (liquids[left], liquids[right])
    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        break

print(ans[0], ans[1])

