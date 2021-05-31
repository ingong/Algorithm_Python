x = 13
total = 0
# answer = True

# for i in int(x):
#     total += int(i)
#
# if x % total != 0:
#     answer = False

# 다른 좋은 풀이
print(x % sum([int(j) for j in str(x)]) == 0)
