class Solution:
    def dp(self,A,B,C,i,j,k,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0 or  j == 0 or k == 0:
            ans = 1

        elif i == 0 and (j == 0 or k == 0):
            ans = 0

        elif A[i-1] == C[k-1] and B[j-1] != C[k-1]:
            ans = self.dp(A,B,C,i-1,j,k-1,dp)

        elif B[j-1] == C[k-1] and A[i-1] != C[k-1]:
            ans = self.dp(A,B,C,i,j-1,k-1,dp)

        elif A[i-1] == C[k-1] and B[j-1] == C[k-1]:
            ans = self.dp(A,B,C,i-1,j,k-1,dp) or self.dp(A,B,C,i,j-1,k-1,dp)
        else:
            ans = 0

        dp[i][j] = ans
        return ans

    def Solve(self,A,B,C):
        m = len(A)
        n = len(B)
        o = len(C)
        if o != m+n:
            return 0

        dp = [[0]*(n+1) for _ in range(m+1)]
        return self.dp(A,B,C,m,n,o,dp), dp

    def isInterleave(self,A,B,C):
        m = len(A)
        n = len(B)
        o = len(C)
        if o != m+n:
            return 0

        dp = [[0]*(n+1) for _ in range(n+1)]

        k = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == C[k-1] and B[j-1] != C[k-1]:
                    dp[i][j] = dp[i+1][j]
                    k += 1
                elif B[j-1] == C[k-1] and A[i-1] != C[k-1]:
                    dp[i][j] = dp[i][j+1]
                    k += 1

                elif A[i-1] == C[k-1] and B[j-1] == C[k-1]:
                    dp[i][j] = dp[i+1][j] or dp[i][j+1]
                    k += 1

        return dp



if __name__ == '__main__':
    A = "a"
    B = ""
    C = "c"
    D = Solution()
    print(D.Solve(A,B,C))
    #print(D.isInterleave(A,B,C))
