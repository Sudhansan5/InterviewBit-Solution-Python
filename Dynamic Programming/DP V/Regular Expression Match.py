import sys

sys.setrecursionlimit(10 ** 9)


class Solution:
    def dp(self,A,B,i,j,aux):
        if aux[i][j] != -1:
            return aux[i][j]
        ans = 0
        if i == 0 and j == 0:
            ans = 1

        elif j == 0:
            ans = 0

        elif i == 0:
            if B[j-1] == '*':
                ans = self.dp(A,B,i,j-1,aux)

        elif A[i-1] == B[j-1] or B[j-1] == '?':
            ans =  self.dp(A,B,i-1,j-1,aux)

        elif B[j-1] == '*':
            ans = self.dp(A,B,i-1,j,aux) or self.dp(A,B,i,j-1,aux)
        else:
            ans = 0

        aux[i][j] = ans
        return ans

    def Solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.dp(A, B, m, n, dp)

    def isMatch(self,A,B):
        m = len(A)
        n = len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1

                elif i == 0:
                    if B[j-1] == '*':
                        dp[i][j] = dp[i][j-1]

                elif j == 0:
                    dp[i][j] = 0

                elif B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                elif A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]


if __name__ == '__main__':
    A = "cabbbac"
    B = "b*a*?*"
    C = Solution()
    print(C.Solve(A, B))
    print(C.isMatch(A,B))
