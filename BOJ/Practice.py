def solution(num):
    count = 0
    while num != 1:
        num = num / 2
        print('1 num : ', num)
        if num == 4:
            print('2 num : ', num)
            return num

solution(16)