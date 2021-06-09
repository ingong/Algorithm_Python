# 중복되는 값과 불필요한 값 입력을 지양해야한다
# 모든 브루트포스는 문제에서 해야하는 방법이 주어진다
# 몇 번, 어떤 채널로 이동해야하는지 알 수 없다 => 이건 방법을 의미한다
#
# 문제의 제한 조건
# N 과 C 의 조건
# C 가 1000000 인건 인상적이다
#
# 시간 복잡도가 같으면 구현하기 쉬운 문제로 => 1번이 쉽지
# 1. 채널 C 로 이동하고, + 또는 - 로 이동하는 방법
# 2. 고장나지 않은 버튼을 이용해서 이동할 수 있는 채널 C 를 만듦
#
# 이렇게 풉시다
# 1. 이동할 채널 C 를 정한다
# 2. C 에 포함되어있는 숫자 중에 고장난 버튼이 있는지 확인
# 3. 고장난 버튼이 포함되어 있지 않다면, C - N 을 계산해서 +, - 버튼을 몇번씩 눌러야하는

n = int(input())
m = int(input())
broken = [False for _ in range(10)]
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    broken[x] = True


def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1

    l = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    return l


ans = abs(n - 100)
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > press + l:
            ans = press + l

print(ans)