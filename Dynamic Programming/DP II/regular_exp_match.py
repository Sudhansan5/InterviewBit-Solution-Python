class Solution:
    def dp(self,A,B,i,j,aux): #Memoization
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i == 0 and  j == 0:
            return 1
        if i == 0 or j == 0:
            return 0
        if A[i-1] == B[j-1] or B[j-1] == '?':
            ans = self.dp(A,B,i-1,j-1,aux)
        elif B[j-1] == '*':
            ans = self.dp(A,B,i-1,j,aux) if self.dp(A,B,i-1,j,aux) else self.dp(A,B,i,j-1,aux)
        else:
            ans=0
        aux[i][j] = ans
        return ans

    def Solve(self,A,B):
        A='_'+A
        B='_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        self.dp(A,B,m,n,dp)
        return dp[m][n]

    def isMatch(self,A,B): #Tabulation
        A='_'+A
        B='_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] if dp[i-1][j] else dp[i][j-1]
        return dp[m][n]

A='bcaccbabaa'
B='bb*c?c*?'
C=Solution()
print(C.Solve(A,B))
print(C.isMatch(A,B))
