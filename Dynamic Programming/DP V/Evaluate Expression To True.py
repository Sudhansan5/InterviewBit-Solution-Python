class Solution:
    def dp(self, s, i, j, isTrue, dp):
        if i > j: return False

        if i == j:
            return s[i] == 'T' if isTrue else s[i] == 'F'

        key = str(i) + str(j) + str(isTrue)
        if key in dp:
            return dp[key]

        ans = 0
        for k in range(i + 1, j, 2):

            lTrue = self.dp(s, i, k - 1, True, dp)
            lFalse = self.dp(s, i, k - 1, False, dp)

            rTrue = self.dp(s, k + 1, j, True, dp)
            rFalse = self.dp(s, k + 1, j, False, dp)

            if s[k] == '&':
                if isTrue:
                    ans += lTrue * rTrue
                else:
                    ans += lFalse * rFalse + lFalse * rTrue + lTrue * rFalse

            elif s[k] == '|':
                if isTrue:
                    ans += lTrue * rFalse + rFalse * lTrue + lTrue * rTrue
                else:
                    ans += lFalse * rFalse

            elif s[k] == '^':
                if isTrue:
                    ans += lTrue * rFalse + lFalse * rTrue
                else:
                    ans += lTrue * rTrue + lFalse * rFalse

        dp[key] = ans
        return ans

    def Solve(self, A):
        n = len(A)
        dp = {}
        return self.dp(A, 0, n - 1, 0, dp), dp


if __name__ == '__main__':
    A = "T^T^T^F|F"
    B = Solution()
    print(B.Solve(A))
