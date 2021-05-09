def solution(inputPriceArr):
    global Price
    answer = 0
    for i in range(InputLen):
        if Price:
            answer += Price // inputPriceArr[i]
            Price = Price % inputPriceArr[i]
    return answer


InputLen, Price = map(int, input().split())
inputArr = [int(input()) for _ in range(InputLen)]
# 해당 풀이에서는 append 를 사용했지만 이 방법이 더 유용하다고 판단한다
inputArr.sort(reverse=True)

# 두 풀이 모두 걸리는 시간은 동일하다