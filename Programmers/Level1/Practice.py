# c, d = max(3, 12), min(3, 12)
c, d = 3, 12
t = 1

while t > 0:
    print('up :', t)
    t = c % d
    c, d = d, t
    print('down :', t)