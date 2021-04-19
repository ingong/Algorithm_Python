# 다른 사람 풀이
def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]

# 내 풀이
def solution(L, x):
    answer = []
    for index, i in enumerate(L):
        if (i == x):
            answer.append(index)
    if len(answer) == 0:
        answer = [-1]
    return answer

