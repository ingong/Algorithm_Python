H, V = 10, 8

horizontal = [4]
horizontal.append(H)

vertical = [2, 3]
vertical.append(V)

h_len = [horizontal[idx] - horizontal[idx-1] for idx, h in enumerate(horizontal) if idx > 0]
v_len = [vertical[idx] - vertical[idx-1] for idx, v in enumerate(vertical) if idx > 0]


answer = -10e9
for h in h_len:
    for v in v_len:
        answer = max(answer, h * v)

print(answer)