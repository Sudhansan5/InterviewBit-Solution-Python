class Solution:
    def dp(self,A,B,i,j,dp):
        global ans

        if dp[i][j]:
            return dp[i][j]

        if i == 0 and j == 0:
            return 1
        if j == 0:
            return 1

        if i == 0:
            return 0

        if A[i-1] == B[j-1]:
            ans = self.dp(A,B,i-1,j-1,dp) + self.dp(A,B, i-1,j,dp)
        else:
            ans =  self.dp(A,B,i-1,j,dp)

        dp[i][j] = ans
        return ans

    def Solve(self, A, B):
        m = len(A)
        n = len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        return self.dp(A,B,m,n,dp)

    def numDistinct(self, A, B):
        m = len(A)
        n = len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1

                elif j == 0:
                    dp[i][j] = 1

                elif A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    A = "rabbbit"
    B = "rabbit"
    C = Solution()
    print(C.Solve(A, B))
    print(C.numDistinct(A, B))
