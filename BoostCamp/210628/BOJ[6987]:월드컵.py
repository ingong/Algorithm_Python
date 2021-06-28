# arr = [5, 0, 0, 3, 0, 2, 2, 0, 3, 0, 0, 5, 4, 0, 1, 1, 0, 4]
arr = [5, 0, 0, 3, 1, 1, 2, 1, 2, 2, 0, 3, 0, 0, 5, 1, 0, 4]
# 3가지 체크
# 1. 각자 나라의 경기 수의 합이 5인지 체크
# 2. 승의 합과 패의 합이 같은지 체크
# 3. 무승부를 확인하는 방법 어떻게 5 1 1 1 1 1
# 합이 짝수인지 확인
# 0 의 개수가 짝수인지 확인

answer = 1

for i in range(0, len(arr), 3):
    if sum(arr[i:i+3]) != 5:
        answer = 0

win, lose = 0, 0
for i in range(0, len(arr), 3):
    win += arr[i]

for i in range(2, len(arr), 3):
    lose += arr[i]

if lose != win:
    answer = 0


count = 0
total = 0
for i in range(1, len(arr), 3):
    if arr[i] != 0:
        count += 1
        total += 1

if total % 2 != 0 or count % 2 != 0:
    answer = 0


print(answer)