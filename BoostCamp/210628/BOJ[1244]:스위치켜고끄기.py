N = int(input())
s = list(map(int, input().split()))
n = int(input())
students = []
for _ in range(n):
    students.append(list(map(int, input().split())))


for student, num in students:
    # 남학생 연
    if student == 1:
        for i, v in enumerate(s):
            if (i + 1) % num == 0:
                s[i] = 1 - v
    else:
        symmetric = 0
        while True:
            # left : num - 1, right : num - 1
            left = num - 1 - symmetric
            right = num - 1 + symmetric
            if left == 0 or right == len(s) - 1:
                break

            if s[left] != s[right]:
                break
            symmetric += 1

        for i in range(num - 1 - symmetric, num + symmetric ):
            s[i] = 1- s[i]
            if s[i] == 0:
                s[i] = 1
            else:
                s[i] = 0

print(s)
