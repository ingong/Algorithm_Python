# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))

N = 5
arr = [[2, 3, 1, 7, 3], [4, 1, 9, 6, 8], [5, 5, 2, 4, 4],[6, 5, 2, 6, 7],[8, 4, 2, 2, 2]]

rev_arr = [[row[i] for row in arr] for i in range(5)]
overlapped = [set() for _ in range(N)]

for i in range(N):
    for j in range(5):
        overlapped[i].update(list(filter(lambda x: rev_arr[j][x] == arr[i][j], range(len(rev_arr[j])))))

person = -10e9
answer = 0
for i in range(len(overlapped)):
    if len(overlapped[i]) > person:
        person = len(overlapped[i])
        answer = i + 1

print(answer)

