#参考链接https://blog.csdn.net/yzy__zju/article/details/98730571
def bag(n, c, w, v):
    dp = [[0] * (c + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if w[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
    return dp[-1][-1]


n = 5
c = 10
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]

print(bag(n, c, w, v))