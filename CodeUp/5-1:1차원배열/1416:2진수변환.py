# num = int(input())
# maxVal = 0
# sum = 0
#
# for i in range(1, num+1):
#     if num - pow(2, i) < 0:
#         maxVal = i - 1
#         break
#
# for i in range(maxVal, -1, -1):
#     if num - pow(2, i) >= 0:
#         num = num - pow(2, i)
#         sum += pow(10, i)
#     else:
#         continue
# print(sum)

# 이 풀이로 가자!
num = int(input())
num = str(bin(num))

print(num[2:])