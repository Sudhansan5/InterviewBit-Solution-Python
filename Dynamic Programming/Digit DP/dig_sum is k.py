class Solution:
    def dp(self, A, B, n, k, pos, lFlag, rFlag, dig_sum, dp):
        if pos == n:
            return dig_sum

        lLim = 0 if lFlag else A[pos]
        rLim = 9 if rFlag else B[pos]

        key = str(lLim) + str(rLim) + str(dig_sum)
        if key in dp:
            return dp[key]
        ans = 0

        for i in range(lLim, rLim+1):
            ans += self.dp(A,B,n, k, pos+1, 1 if i > A[pos] else lFlag, 1 if i < B[pos] else rFlag, dig_sum + i, dp)

        dp[key] = ans
        return ans

    def Solve(self, A, k):
        C = [5]
        n = len(A)
        dp = {}
        return self.dp(A,C,n,k, 0,0,0,0,dp), dp

if __name__ == '__main__':
    A = [1]
    k = 4
    B = Solution()
    print(B.Solve(A, k))
