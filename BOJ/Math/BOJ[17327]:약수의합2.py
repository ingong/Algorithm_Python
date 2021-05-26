# 접근, 로직설계, 풀이 코
# 접근
# 5의 배수는 5를 전부 약수로 가진다
# 1 부터 N 까지 각각의 수 * 그 수를 갖는 약수의 개수
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i * (N // i)
print(sum)