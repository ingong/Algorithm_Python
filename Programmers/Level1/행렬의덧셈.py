A = [[1], [2]]
B = [[3], [4]]
# zip
answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
for a, b in zip(A, B):
    for c, d in zip(a, b):
        print(c + d)

# answer = [[arr1[j][i] + arr2[j][i] for i in range(len(arr1[0]))] for j in range(len(arr1))]
# print(answer)

