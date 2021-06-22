def solution(clothes):
    dic = {}
    temp = 1
    for c, t in clothes:
        if t in dic.keys():
            dic[t] += 1
        else:
            dic[t] = 1

    for i in dic.values():
        temp *= (i + 1)

    return temp - 1