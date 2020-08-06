class Solution:
    def countSetBits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def dp(self, A, n, mask, dp):
        row = self.countSetBits(mask)
        if row == n:
            return 0

        key = str(row)+"->"+str(mask)

        if key in dp:
            return dp[key]

        ans = 0
        for col in range(n):
            if (mask >> col) & 1:
                continue

            ans = max(ans, A[row][col] + self.dp(A, n, mask | (1 << col), dp))
            print(ans)

        dp[key] = ans
        return ans

    def Solve(self, A):
        n = len(A)
        dp = {}
        return self.dp(A, n, 0, dp), dp


if __name__ == '__main__':
    A = [[1, 2, 5],
         [1, 15, 20],
         [1, 1, 10]]

    C = [[5, -1256104, 1278159],
         [3940, -2016, -6565],
         [-1293128, -7034, -1292630]]

    B = Solution()
    print(B.Solve(C))
