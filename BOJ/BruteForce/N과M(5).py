n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
check = [False] * (n + 1)
cnt = [0] * m


def go(index, n, m):
    if index == m:
        print(' '.join(map(str, cnt)))
        return
    for i in range(0, n):
        if check[i]:
            continue
        check[i] = True
        cnt[index] = num_list[i]
        go(index + 1, n, m)
        check[i] = False


go(0, n, m)
# m 은 주어진 총 길이, index 는 0부터 시작해서 m 에서 만나면 끝난다!
