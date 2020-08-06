class Solution:
    def lcs(self,A,B,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]

        if i == 0 or j == 0:
            ans = 0
        elif A[i-1] == B[j-1]:
            ans = 1 + self.lcs(A,B,i-1,j-1,aux)
        else:
            ans = max(self.lcs(A,B,i-1,j,aux), self.lcs(A,B,i,j-1,aux))

        aux[i][j] = ans
        return ans

    def Solve(self,A,B):
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        return self.lcs(A,B,m,n,dp)

    def lcs_tabulation(self,A,B):
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]

A = "abbcdgf"
B = "bbadcgf"
C = Solution()
print(C.Solve(A,B))
print(C.lcs_tabulation(A,B))
