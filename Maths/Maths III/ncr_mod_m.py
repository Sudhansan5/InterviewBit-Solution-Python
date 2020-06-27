class Solution:
    # Memoization
    def dp(self,n,r,p,dp):
        global ans
        if dp[n][r]:
            return dp[n][r]
        if n == r or r == 0:
            ans = 1
        else:
            ans = (self.dp(n-1,r-1,p,dp) + self.dp(n-1,r,p,dp))
        dp[n][r] = ans%p
        return ans%p

    def Solve(self,A,B,C):
        dp=[[0]*(B+1) for _ in range(A+1)]
        self.dp(A,B,C,dp)
        return dp[-1][-1]

    #Tabulation Space-O(n)
    def ncr(self,n,r,p):
        if r > n-r:
            r = n-r
        dp=[0 for _ in range(r+1)]
        dp[0]=1

        for i in range(1,n+1):
            for j in range(min(i,r),0,-1):
                dp[j] = (dp[j] + dp[j-1])%p
        return dp[-1]

    #Tabulation space- O(n^2)
    def ncr_2(self,n,r,p):
        dp=[[0]*(r+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(min(i,r)+1):
                if i == j or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%p
        return dp[-1][-1]


if __name__ == '__main__':
    A=89
    B=58
    C=268
    D=Solution()
    print(D.Solve(A,B,C))
    print(D.ncr(A,B,C))
    print(D.ncr_2(A,B,C))
