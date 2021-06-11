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

        for preRow in range(row):
            if col == cols[preRow] or abs(preRow - row) == abs(cols[preRow] - col):
                isAble = False
                break
            else:
                pass

        if isAble:
            cols[row] = col
            solve(row + 1, N)

solve(0, N)
print(ans)