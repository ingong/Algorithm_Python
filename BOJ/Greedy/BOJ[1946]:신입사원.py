testCase = int(input())
applis = int(input())

for i in range(testCase):
    rankList = []
    for _ in range(applis):
        rankList.append(list(map(int, input().split())))
    maxRank = min(rankList, key=lambda x: x[0])


for i in range(len(rankList)):
    for j in range(testCase):
        check = testCase
        for k in range(len(maxRank)):
            print(maxRank)
            print(rankList)
            if rankList[i][j] > maxRank[k][j]:
                check -= 1
        print(check)
        if check == 0:
            result -= 1

print(result)


# for i in range(applis):
#     for j in range(applis):
#         if rankList[i][0] > rankList[j][0] and rankList[i][1] > rankList[j][1]:
#             checkList[i] = 0
#             break
#
# print(checkList.count(1))
# 전체를 순환하면서 이중 for 문으로 돌거나

# arrayoflists =[[6,2],[3,4],[5,10]]
# new_list = sorted(arrayoflists, key=lambda x:x[0], reverse=True)
# new_list2 = max(arrayoflists, key=lambda x:x[0])
# print(arrayoflists)
# print(new_list2)