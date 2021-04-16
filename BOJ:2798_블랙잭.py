# 1초에 2천만
# 어떻게 비교할 것인가? => 3개 잖아
n, m = list(map(int, input().split(" ")))
cardList = list(map(int, input().split(" ")))

length = len(cardList)
result = 0

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = cardList[i] + cardList[j] + cardList[k]
            if sum_value <= m:
                result = max(sum_value, result)

print(result)