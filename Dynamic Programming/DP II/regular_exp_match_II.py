class Solution:
    def Solve(self,A,B):
        A='_'+A
        B='_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1] or B[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif B[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if A[i-1] == B[j-2] or B[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]

A='baaaaaabaaaabaaaaababababbaab'
B='..a*aa*a.aba*a*bab*'
C=Solution()
print(C.Solve(A,B))
