test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

# 알아둬야할 포인트
# for _ in range(test_case) 라는 코드를 통해 원하는 반복 수만큼 실행
# queue = [(i, idx) for idx, i in enumerate(queue)] 이런식으로 queue 를 재선언함으로써 index 와 값에 모두 접근하게함
# lambda 표현식을 통해 tuple 의 첫 번째 요소 중 가장 큰 놈을 찾는다! => key = lambda x: x[0]

# 내가 이해한 코드의 의도
# 한 번 입력받으면 코드가 실행되게 하며, 원할 때까지 반복하므로 while 문을 실행
# count 변수를 통해 몇 번째로 출력되는지 확인하게 변수로 지정!

# 궁금한 포인트
# 어떻게 시간 복잡도를 계산하는지 궁금하다
