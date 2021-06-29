def isPalin(x):
    if x == x[::-1]:
        return True
    else:
        return False


def isPseudoPalin(x):
    for i, v in enumerate(x):
        nx = x[:i] + x[i + 1:]
        if nx == nx[::-1]:
            return True
        else:
            continue

    return False


def solution():
    words = []
    words.extend(["abba", "summuus", "xabba", "xabbay", "comcom"])
    for w in words:
        if isPalin(w):
            print(0)
        elif isPseudoPalin(w):
            print(1)
        else:
            print(2)



solution()
# N = int(input())
# for _ in range(N):
#      words.append()