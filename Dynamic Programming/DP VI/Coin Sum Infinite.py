class Solution:
    def dp(self, A, rem, index, dp):
        mod = 10 ** 6 + 7
        if rem == 0: return 1
        if index == len(A) or rem < 0:
            return 0

        if (rem,index) in dp:
            return dp[(rem,index)]

        pick = self.dp(A,rem-A[index], index, dp)
        dont = self.dp(A, rem, index+1,dp)

        dp[(rem,index)] = (pick + dont)%mod
        return dp[(rem,index)]

    def Solve(self, A, B):
        dp = {}
        return self.dp(A,B,0,dp), dp

    def coinChange(self,A,B):
        mod = 10 ** 6 + 7
        dp = [0 for _ in range(B+1)]
        dp[0] = 1
        for i in A:
            for j in range(i,B+1):
                if i <= j:
                    dp[j] += dp[j-i]
                    dp[j] %= mod

        return dp[-1]

if __name__ == '__main__':
    A = [18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8]
    B = 458
    C = Solution()
    print(C.Solve(A, B))
    print(C.coinChange(A,B))
