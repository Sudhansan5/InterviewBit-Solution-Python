class Solution:
    def dp(self,A,B,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i==0:
            return j
        if j==0:
            return i

        if A[i-1] == B[j-1]:
            ans = self.dp(A,B,i-1,j-1,aux)
        else:
            ans = 1 + min(self.dp(A,B,i-1,j-1,aux), self.dp(A,B,i-1,j,aux), self.dp(A,B,i,j-1,aux))
        aux[i][j] = ans
        return ans

    def tabulation(self,A,B):
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    def Solve(self,A,B):
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        b=self.dp(A,B,m,n,dp)
        return b if m < 1 or n < 1 else dp[m][n]

A = "anshuman"
B = "antihuman"
C = Solution()
print(C.Solve(A,B))
print(C.tabulation(A,B))
