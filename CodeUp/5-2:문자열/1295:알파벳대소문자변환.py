charList = list(input())
for i in range(len(charList)):
    if type(charList[i]) != 'str':
        pass

    if charList[i].isupper():
        charList[i] = charList[i].lower()

    elif charList[i].islower():
        charList[i] = charList[i].upper()

print("".join(charList))