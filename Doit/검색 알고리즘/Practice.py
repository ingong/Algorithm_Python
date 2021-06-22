def search(b, key):
    pl = 0
    pr = len(b) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if b[pc] == key:
            return pc
        elif b[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1


a = [1, 2, 3, 4, 5]
b = a[:]
key = 3
answer = search(b, key)
print(answer)
