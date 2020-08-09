class Solution:
    def dp(self, A, i, j, dp):
        m = len(A)
        n = len(A[0])
        if dp[i][j] != float('inf'):
            return dp[i][j]

        if i == m or j == n:
            return float('inf')

        if i == m-1 and j == n-1:
            hp = 1 - A[i][j] if A[i][j] <= 0 else 1
        else:
            hp = min(self.dp(A,i+1,j,dp), self.dp(A,i,j+1,dp)) - A[i][j]

        dp[i][j] = 1 if hp <= 0 else hp
        return dp[i][j]


    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        return self.dp(A,0,0,dp)

    def calculateMinimumHP(self,A):
        m = len(A)
        n = len(A[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - A[i][j], 1)

        return dp[0][0]


if __name__ == '__main__':
    A = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]

    B = Solution()
    print(B.Solve(A))
    print(B.calculateMinimumHP(A))
