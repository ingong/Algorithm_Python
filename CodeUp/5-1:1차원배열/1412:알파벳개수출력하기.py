str = input()
li = [0 for _ in range(26)]
for i in str:
    if i >= 'a' and i <= 'z':
        li[ord(i) - 97] += 1

for i in range(26):
    print("%c:%d" % (chr(i + 97), li[i]))