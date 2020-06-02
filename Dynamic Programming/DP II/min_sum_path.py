class Solution:
    def dp(self,A,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i == 0 and j == 0:
            ans = A[i][j]
            return ans
        if i == 0 or j == 0:
            if i == 0:
                ans = self.dp(A,i,j-1,aux) + A[i][j]
            else:
                ans = self.dp(A,i-1,j,aux) + A[i][j]
        else:
            ans = min(self.dp(A,i-1,j,aux),self.dp(A,i,j-1,aux)) + A[i][j]
        aux[i][j] = ans
        return ans

    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        dp=[[0]*(n) for _ in range(m)]
        self.dp(A,m-1,n-1,dp)
        return dp[m-1][n-1]

    def minPathSum(self,A):
        m=len(A)
        n=len(A[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = A[i][j]
                elif i == 0 or j == 0:
                    if i == 0:
                        dp[i][j] = dp[i][j-1] + A[i][j]
                    else:
                        dp[i][j] = dp[i-1][j] + A[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + A[i][j]
        return dp[m-1][n-1]

A = [[1, 3, 2],
     [4, 3, 1],
     [5, 6, 1]]
B = Solution()
print(B.Solve(A))
print(B.minPathSum(A))
