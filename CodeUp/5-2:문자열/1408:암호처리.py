str = input()

for i in str:
    print(chr(ord(i)+2), end="")

print()
for i in str:
    print(chr((ord(i)*7) % 80 + 48), end="")
