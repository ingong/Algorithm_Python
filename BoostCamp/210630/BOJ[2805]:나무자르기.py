N, target = 4, 7
trees = [20, 15, 10, 17]
trees.sort()
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree - mid > 0:
            total += (tree - mid)
            # print(total)

    if total >= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)

