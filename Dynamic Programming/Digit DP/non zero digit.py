class Solution:
    def dp(self, A, n, pos, flag, non_zero, dp):
        if pos == n:
            return 1

        lim = 9 if flag else A[pos]
        ans = 0

        key = str(pos) + str(flag) + str(non_zero)
        if key in dp:
            return dp[key]

        for i in range(lim + 1):
            if i != 0 and non_zero == 3:
                continue

            ans += self.dp(A, n, pos + 1, 1 if i < A[pos] else flag,
                           non_zero + 1 if i != 0 else non_zero, dp)

        dp[key] = ans
        return ans

    def Solve(self, A):
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
    A = ["1109", "1115"]
    B = Solution()
    print(B.Solve(A))
