money = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]
answer = 0

for i in change:
    if money == 0:
        break
    answer += money // i
    money = money % i
print(answer)
# 나머지가 나오게 하고, count 에는 몫이 들어가게한다
# 언제까지? money 가 0 원이 될 때까지
# money 를 나눌 수 있을 만큼 나눈다
# 몫 만큼 count 에 더 해준다