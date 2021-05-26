bracket = list(input())
left = 0
right = 0
for i in range(len(bracket)):
    if bracket[i] == "(":
        left += 1
right = len(bracket) - left
print(left, right)

