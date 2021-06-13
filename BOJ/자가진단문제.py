# 1
# A B

# 2
# 71

# 3번
# 15
count = 0
for i in range(1, 100, 7):
    print(i)
    count += 1
    print(count)
print(count)

# 4번
# 5

# 5번
# 5

# 6번
arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr2 = [3, 2, 4, 4, 2, 5, 2, 5, 5]
overlap = {}

for number in sorted(arr):
    if number in overlap:
        overlap[number] += 1
    else:
        overlap[number] = 1

if not overlap:
    print([-1])
else:
    print(list(filter(lambda x: x > 1, list(overlap.values()))))
