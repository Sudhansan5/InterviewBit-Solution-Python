class Solution:
    def lcs(self,A,B,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0 or j == 0:
            return 0

        if A[i-1] == B[j-1] and i-1 != j-1:
            ans = 1 + self.lcs(A,B,i-1,j-1,dp)
        else:
            ans = max(self.lcs(A,B,i-1,j,dp), self.lcs(A,B,i,j-1,dp))

        dp[i][j] = ans
        return ans

    def Solve(self,A):
        n =len(A)
        dp = [[0]*(n+1) for _ in range(n+1)]
        self.lcs(A,A,n,n,dp)

        if dp[-1][-1] >= 1:
            return 1
        else:
            return 0

    def anytwo(self,A):
        n = len(A)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if A[i-1] == A[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if dp[-1][-1] >= 2:
            return 1
        return 0

if __name__ == '__main__':
    A = "abab"
    B = Solution()
    print(B.Solve(A))
    print(B.anytwo(A))
