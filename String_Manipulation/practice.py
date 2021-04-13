import sys
userInput = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ascending = True
descending = True

for i in range(1, 8):
    if userInput[i] > userInput[i - 1]:
        descending = False
    if userInput[i] < userInput[i - 1]:
        ascending = False

if ascending:
    answer = "ascending"
elif descending:
    answer = "descending"
else:
    answer = "mixed"

print(answer)




