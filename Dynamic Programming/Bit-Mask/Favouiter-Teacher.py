class Solution:
    def countSetBits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def dp(self, A, mask, dp):
        pos = self.countSetBits(mask)

        if pos == len(A):
            return 1

        if mask in dp:
            return dp[mask]

        ans = 0
        for j in range(len(A)):
            if ((mask >> j) & 1) == 0:
                A[pos][j] = 1
            ans += self.dp(A, (mask | (1 << j)), dp)

        dp[mask] = ans
        return ans

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = {}
        return self.dp(A, 0, dp)


if __name__ == '__main__':
    A = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

    B = Solution()
    print(B.Solve(A))
