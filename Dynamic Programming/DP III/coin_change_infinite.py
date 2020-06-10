class Solution:
    def Solve(self,A,B):
        dp=[0]*(B+1)
        dp[0]=1
        for i in A:
            for j in range(1,B+1):
                if i <= j:
                    dp[j] = dp[j] + dp[j-i]
        return dp

A=[1,2,5]
B=11
C=Solution()
print(C.Solve(A,B))
