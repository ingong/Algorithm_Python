N, K = 20, 1
array = 'HHPHPPHHPPHPPPHPHPHP'
check = [2 if v == 'H' else 0 for v in array]

for i, v in enumerate(check):
    if v == 2:
        start = i - K
        end = i + K + 1
        if start < 0:
            start = 0
        if end >= len(check):
            end = len(check) - 1

        for p in range(start, end):
            if check[p] == 0:
                check[p] = 1
                break
    else:
        continue

print(check.count(1))