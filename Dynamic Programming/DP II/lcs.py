class Solution:
    def lcs(self,A,B,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]

        if i == 0 or j==0:
            return 0
        if A[i] == B[j]:
            ans = 1 + self.lcs(A,B,i-1,j-1,aux)
        else:
            ans = max(self.lcs(A,B,i-1,j,aux), self.lcs(A,B,i,j-1,aux))
        aux[i][j] = ans
        return ans

    def lcs_tabulation(self,A,B):
        A = '_'+A
        B = '_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]

    def Solve(self,A,B):
        A = '_'+A
        B = '_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*n for _ in range(m)]
        self.lcs(A,B,m-1,n-1,dp)
        return dp[m-1][n-1]

A = "abbcdgf"
B = "bbadcgf"
C = Solution()
print(C.Solve(A,B))
print(C.lcs_tabulation(A,B))
