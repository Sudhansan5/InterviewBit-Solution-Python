class Solution:
    def dp(self, B, C, i, j, dp): # Not working
        global ans
        if j == 0:
            dp[j][0] = 0
            return dp[j][0]

        if i < 0: return float('inf')

        if dp[j][i] != float('inf'):
            return dp[j][i]

        if i - B[j - 1] >= 0:
            pick = self.dp(B, C, i - B[j - 1], j, dp) + C[j - 1]
            dont = self.dp(B, C, i, j - 1, dp)
            ans = min(pick, dont)
        else:
            ans = self.dp(B, C, i, j - 1, dp)

        dp[j][i] = ans
        return ans

    def Solve(self, A, B, C):
        n = len(B)
        m = max(A)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        return self.dp(B, C, m, n, dp), dp

    def party(self, A, B, C):
        n, m = len(B) + 1, max(A) + 1
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 0

        for i in range(m):
            for j in range(1, n):
                if i - B[j - 1] >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - B[j - 1]][j] + C[j - 1])
                else:
                    dp[i][j] = dp[i][j - 1]

        ans = 0
        for i in A:
            ans += dp[i][-1]

        return ans


if __name__ == '__main__':
    A = [2, 4, 6]
    B = [2, 1, 3]
    C = [2, 5, 3]
    D = Solution()
    print(D.Solve(A, B, C))
    # print(D.party(A,B,C))
