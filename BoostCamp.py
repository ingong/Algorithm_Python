# ACMP 호
# H, W, N = 30, 50, 72
# floor = N % H
# room = 0
# print(N//H + 1)
# if len(str(N//H + 1)) > 1:
#     room = (N // H)
# else:
#     room = "0" + str(N//H + 1)
#
# answer = "".join([str(floor), str(room)])
# print(answer)

# N = 4
# first_num = [4, 6, 9, 19]
# pads = [[0 for _ in range(i+1)] for i in range(N)]
#
# for i in range(N):
#     pads[i][0] = first_num[i]
#
# for i in range(1, N):
#     for j in range(1, i+1):
#         pads[i][j] = pads[i][j-1] - pads[i-1][j-1]

# 더하기 싸이클
# N = 26
# final = N
# count = 0
#
# if N < 10:
#     N = "0" + str(N)
# else:
#     pass
#
#
# while True:
#     first_N = str(N)[-2]
#     last_N = str(N)[-1]
#     Sum = "0" + str(int(first_N) + int(last_N))
#     new_N = last_N + str(Sum)[-1]
#     N = new_N
#     count += 1
#
#     if N == str(final):
#         break
# print(count)


# O, X 퀴즈
# problem = "OOXXOXXOOO"
# p_length = len(problem)
# score = [0 for _ in range(p_length)]
#
# if problem[0] == "O":
#     score[0] = 1
#
# for i in range(1, p_length):
#     if problem[i] == "O":
#         score[i] = score[i-1] + 1
#     else:
#         continue
#
# answer = sum(score)
# print(answer)

# A = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
# B = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
#
# result = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
# print(result)

array = [1, 5, 2, 6, 3, 7, 4]
abc = list(map(str, array))
print(abc)

