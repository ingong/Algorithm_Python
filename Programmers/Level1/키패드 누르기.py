# 1, 4, 7, * 왼손
# 3, 6, 9, # 오른손
# 2, 5, 8, 0 => 1. 가까운 => L 과 R 이 어디에 위치해있는지, 거리를 산출해야함 (col) 2. 동일하다면 본인의 선호하는 손가락
def solution(numbers, hand):
    answer = ''
    keypads = {}
    keypads['*'] = (3, 1)
    keypads[0] = (3, 2)
    keypads['#'] = (3, 3)
    for i in range(1, 10):
        if i not in keypads:
            keypads[i] = 0
        if i % 3 == 0:
            keypads[i] = ((i - 1) // 3, 3)
        else:
            keypads[i] = ((i - 1) // 3, i % 3)
    l, r = '*', '#'

    for i in range(len(numbers)):
        if numbers[i] in (1, 4, 7):
            answer += "L"
            l = numbers[i]
        elif numbers[i] in (3, 6, 9):
            answer += "R"
            r = numbers[i]
        else:
            dist1 = sum([abs(a - b) for a, b in zip(keypads[numbers[i]], keypads[l])])
            dist2 = sum([abs(a - b) for a, b in zip(keypads[numbers[i]], keypads[r])])

            if dist1 > dist2:
                answer += "R"
                r = numbers[i]
            elif dist1 < dist2:
                answer += "L"
                l = numbers[i]
            else:
                if hand == "right":
                    answer += "R"
                    r = numbers[i]
                else:
                    answer += "L"
                    l = numbers[i]

    return answer