class Solution:
    def dp(self, A, n, d, k, pos, flag, dig_sum, dp):
        if dig_sum > k: return 0

        if pos == n:
            return dig_sum == k

        lim = 9 if flag else A[pos]
        ans = 0

        key = str(pos) + str(flag) + str(dig_sum)
        if key in dp:
            return dp[key]

        for i in range(lim+1):
            if pos % 2 != 0 and i != d: continue
            ans += self.dp(A,n,d,k,pos+1, 1 if i < A[pos] else flag, dig_sum+i, dp)

        dp[key] = ans
        return ans


    def Solve(self,A, d, k):
        n = len(A)
        dp = {}
        return self.dp(A, n, d, k, 0, 0, 0, dp), dp

if __name__ == '__main__':
    A = [1,2,3,4]
    d = 1
    k = 4
    B = Solution()
    print(B.Solve(A, d, k))
