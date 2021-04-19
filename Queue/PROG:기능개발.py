def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


result = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
print(result)


# point
# if 와 while 을 적절하게 활용
# time 변수를 적절하게 활용할 필요가 있다



# pseudo code
# while (progresses 가 빌때까지)
#     if (progresses 첫 요소 계산 값이 100 보다 클 때)
#         progresses, speeds 꺼낸다
#         count 1 더한다
#     else
#         if (count > 0)
#             count 를 answer에 넣기
#             count 를 0 으로 초기화
#         time 1 더해준다
#     count 를 answer 에 넣기