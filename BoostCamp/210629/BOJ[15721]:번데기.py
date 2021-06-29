import sys
input = sys.stdin.readline

people = int(input())
number = int(input())
word = int(input())

n = 2
count = 0
start = ['뻔', '데기', '뻔', '데기']
result = []

while True:
    repeat = ["뻔"] * n + ["데기"] * n
    result += (start + repeat)
    if len(result) > 10000:
        break
    n += 1

if word == 0:
    keyword = "뻔"
else:
    keyword = "데기"

for i, val in enumerate(result):
    if val == keyword:
        count += 1
    if count == number:
        print(i)
        print(people)
        print((i % people))
        break

