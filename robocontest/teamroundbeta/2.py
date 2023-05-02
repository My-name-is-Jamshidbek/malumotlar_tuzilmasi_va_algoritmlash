MOD = 1000000007

n = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]

for j in range(1, n+1):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(1, n+1):
        for k in range(1, j):
            if (k % 2 == 0 and j % 2 == 1) or (k % 2 == 1 and j % 2 == 0):
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

ans = 0
for j in range(1, n+1):
    ans = (ans + dp[n][j]) % MOD

print(ans)
