# N = 5
# arr1 = [[2, 3, 1, 7, 3], [4, 1, 9, 6, 8], [5, 5, 2, 4, 4],[6, 5, 2, 6, 7],[8, 4, 2, 2, 2]]

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

rev_arr = [[row[i] for row in arr] for i in range(5)]
overlapped = [set() for _ in range(N)]

for i in range(N):
    for j in range(5):
        overlapped[i].update(list(filter(lambda x: rev_arr[j][x] == arr[i][j], range(len(rev_arr[j])))))


sorted_overlapped = sorted(overlapped, reverse=True, key=lambda x: (len(x), x))
print("".join([str(i + 1) for i, val in enumerate(overlapped) if val == sorted_overlapped[0]]))

# print(rev_arr[j])
# print(arr[i][j])

# print([i for i, val in enumerate(rev_arr[j]) if val == arr[i][j]])

