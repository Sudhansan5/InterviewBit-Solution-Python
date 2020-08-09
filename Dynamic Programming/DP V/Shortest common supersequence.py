class Solution:
    def lcs(self,A,B):
        m = len(A)
        n = len(B)
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + A[i]

                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)

        return dp[-1][-1]

    def Solve(self, C):
        val = C.split("  ")
        A = val[0]
        B = val[1]

        lcs = self.lcs(A,B)
        i,j = 0, 0
        ans = ""
        for c in lcs:
            while A[i] != c:
                ans += A[i]
                i += 1

            while B[j] != c:
                ans += B[j]
                j += 1

            ans += c
            i += 1
            j += 1

        return ans + A[i:] +B[j:]



if __name__ == '__main__':
    A = 'abac  cab'
    C = Solution()
    print(C.Solve(A))
