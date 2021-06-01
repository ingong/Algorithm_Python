# without library
import sys
input = sys.stdin.readline
n = int(input())
queue = [0] * n
begin = 0
end = 0

# *val 이라는 의미는 인자를 몇개를 받을 지 모를 때 사용한다
# 즉, 변수를 받을 수도 받지 않을 수도 있는 것이다
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        queue[end] = num
        end += 1
    elif cmd == 'front':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
    elif cmd == 'size':
        print(end-begin)
    elif cmd == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
            begin += 1
    elif cmd == 'back':
        if begin == end:
            print(-1)
        else:
            print(queue[end-1])