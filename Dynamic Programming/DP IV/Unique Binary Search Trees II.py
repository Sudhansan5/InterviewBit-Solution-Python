class Solution:
    def dp(self, n, dp):
        if n <= 1:
            return 1

        if dp[n]:
            return dp[n]

        ans = 0
        for i in range(1, n+1):
            ans += self.dp(i-1, dp) * self.dp(n-i, dp)

        dp[n] = ans
        return ans

    def Solve(self, A):
        dp = [0 for _ in range(A+1)]
        return self.dp(A,dp)

if __name__ == '__main__':
    A = 10
    B = Solution()
    print(B.Solve(A))
