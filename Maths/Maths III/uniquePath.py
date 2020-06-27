class Solution:
    def dp(self,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]
        if i == 1 or j == 1:
            ans = 1
        else:
            ans = self.dp(i-1,j,dp) + self.dp(i,j-1,dp)
        dp[i][j] = ans
        return ans

    def Solve(self,A,B):
        dp=[[0]*(B+1) for _ in range(A+1)]
        self.dp(A,B,dp)
        return dp[-1][-1]

    def uniqePath(self,A,B):
        dp=[1 for _ in range(B)]
        for i in range(A-1):
            for j in range(1,B):
                dp[j] += dp[j-1]
        return dp[-1]

    def uniquePaths(self,A,B):
        path=1
        for i in range(B,(A+B-1)):
            path *= i
            path //= i-B+1
        return path

if __name__ == '__main__':
    A=2
    B=2
    C=Solution()
    print(C.Solve(A,B))
    print(C.uniqePath(A,B))
    print(C.uniquePaths(A,B))
