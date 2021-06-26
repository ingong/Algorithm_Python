def solution(n, money):
    money.sort()
    dp = [1 if i % money[0] == 0 else 0 for i in range(n + 1)]

    for i in range(1, len(money)):
        for j in range(money[i], n + 1):
            dp[j] += dp[j - money[i]]

    return dp[n]