N = int(input())
cols = [-1 for _ in range(N)]
ans = 0

def solve(row, N):
    global ans
    if row == N:
        ans += 1
        return

    for col in range(N):
        isAble = True

        for prevRow in range(row):
            if col == cols[prevRow] or abs(prevRow-row) == abs(cols[prevRow] - col):
                isAble = False
                break

        if isAble:
            cols[row] = col
            solve(row + 1, N)


solve(0, N)
print(ans)