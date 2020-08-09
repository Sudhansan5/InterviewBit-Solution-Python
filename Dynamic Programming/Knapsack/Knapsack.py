class Solution:
    def dp(self, w, n, wt, val, dp):
        global ans
        if n == 0: return 0
        if not wt: return 0

        if dp[n][w]: return dp[n][w]

        if wt[n - 1] > w:
            ans = self.dp(w, n - 1, wt, val, dp)
        else:
            pick = val[n - 1] + self.dp(w - wt[n - 1], n - 1, wt, val, dp)
            dont = self.dp(w, n - 1, wt, val, dp)
            ans = max(pick, dont)

        dp[n][w] = ans
        return ans

    def Solve(self, wt, val, w):
        n = len(wt)
        dp = [[0] * (w + 1) for _ in range(n + 1)]
        return self.dp(w, n, wt, val, dp)

    def knapsack(self, wt, val, w):
        n = len(wt)
        dp = [[0] * (w + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for w1 in range(w + 1):
                if i == 0 or w1 == 0:
                    dp[i][w1] = 0

                elif wt[i - 1] > w1:
                    dp[i][w1] = dp[i - 1][w1]
                else:
                    dp[i][w1] = max(dp[i - 1][w1], val[i - 1] + dp[i - 1][w1 - wt[i - 1]])

        return dp[-1][-1]


if __name__ == '__main__':
    A = [1, 3, 4, 5]  # wt
    B = [1, 4, 5, 7]  # val
    C = 7  # w
    D = Solution()
    # print(D.Solve(A, B, C))
    print(D.knapsack(A, B, C))
