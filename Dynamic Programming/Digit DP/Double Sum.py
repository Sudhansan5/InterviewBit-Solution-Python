class Solution:
    def dp(self, A, n, pos, flag, dig_sum, dp):
        mod = 10 ** 9 + 7
        if pos == n:
            return dig_sum

        lim = 9 if flag else A[pos]
        key = str(pos) + str(flag) + str(dig_sum)
        if key in dp:
            return dp[key]

        ans = 0
        for i in range(lim + 1):
            ans += self.dp(A, n, pos + 1, 1 if i < A[pos] else flag, dig_sum + i, dp)
            ans %= mod

        dp[key] = ans
        return ans

    def Solve(self,A):
        mod = pow(10, 9) + 7
        n = len(A)
        ans = []
        for i in range(n // 2):
            dp = {}

            start = str(int(A[2 * i]) - 1)
            start = [int(i) for i in start]

            end = A[2 * i + 1]
            end = [int(i) for i in end]

            h = self.dp(end, len(end), 0, 0, 0, dp)
            dp.clear()
            l = self.dp(start, len(start), 0, 0, 0, dp)
            ans.append((h - l) % mod)

        return ans

if __name__ == '__main__':
    A = ["88", "114", "12", "5706", "18", "6318", "371", "60047", "65", "56234"]
    B = Solution()
    print(B.Solve(A))
