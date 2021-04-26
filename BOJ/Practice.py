# 1부터 100까지 더하기
# 1. top-down (반복문으로)
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 2. 재귀 함수
def addRecur(num):
    if num <= 1:
        return 1
    return num + addRecur(num-1)


print(addRecur(100))

