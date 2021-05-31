a, b = 5, 3
print(("*" * a + "\n") * b)

# 내 풀이
for j in range(b):
    for i in range(a):
        if i == a - 1:
            print("*")
        else:
            print("*", end="")
