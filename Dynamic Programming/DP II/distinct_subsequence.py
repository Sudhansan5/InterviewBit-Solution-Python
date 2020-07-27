class Solution:
    def dp(self, A, B, i, j, aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i == 0 and j == 0:
            return 1
        if i == 0:
            return 0
        if j == 0:
            return 1
        if A[i - 1] == B[j - 1]:
            ans = self.dp(A, B, i - 1, j - 1, aux) + self.dp(A, B, i - 1, j, aux)
        else:
            ans = self.dp(A, B, i - 1, j, aux)
        aux[i][j] = ans
        return ans

    def Solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        self.dp(A, B, m, n, dp)
        return dp[m][n]

    def numDistinct(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 or j == 0:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    if A[i - 1] == B[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1]


A = 'rabbbit'
B = 'rabbit'
C = Solution()
print(C.Solve(A, B))
print(C.numDistinct(A, B))
