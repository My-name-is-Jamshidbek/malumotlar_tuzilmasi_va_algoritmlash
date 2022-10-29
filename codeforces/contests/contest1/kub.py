n = int(input())
f = int(input())
DP = [[0 for j in range(4)] for i in range(1001)]
DP[2][3] = 8
for i in range(3, n + 1):
    DP[i][3] = DP[i - 1][3]
    DP[i][2] = DP[i - 1][2] + 12
    DP[i][1] = DP[i - 1][1] + DP[i - 1][2] + 6
    DP[i][0] = DP[i - 1][0] + DP[i - 1][1] // 2 + DP[i - 1][2] // 4 + 1
print(DP[n][f])



