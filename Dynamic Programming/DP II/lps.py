class Solution:
    def lps(self,A,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i == j:
            return 1
        if i > j:
            return 0
        if A[i] == A[j]:
            ans = 2 + self.lps(A,i+1,j-1,aux)
        else:
            ans = max(self.lps(A,i+1,j,aux),self.lps(A,i,j-1,aux))
        aux[i][j] = ans
        return ans

    def lps_tabulation(self,A):
        n=len(A)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
                dp[i][i] = 1
                
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if A[i] == A[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

    def Solve(self,A):
        n=len(A)
        dp=[[0]*n for _ in range(n)]
        self.lps(A,0,n-1,dp)
        return dp[0][n-1]

A = "bebeeed"
B = Solution()
print(B.Solve(A))
print(B.lps_tabulation(A))
