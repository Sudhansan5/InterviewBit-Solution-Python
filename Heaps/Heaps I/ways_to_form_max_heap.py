import math
class Solution:
    def __init__(self):
        self.mod=1000000007

    def combination(self,n,k):
        ans=[[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(min(i,k)+1):
                if j==0 or j==i:
                    ans[i][j]=1
                else:
                    ans[i][j] = (ans[i-1][j-1] + ans[i-1][j]) % self.mod
        return ans

    def left_node(self,n):
        if n==1:
            return 0

        h = int(math.log2(n))
        last = (1 << h) #2^h
        curr = n - ((1 << h) - 1)
        if curr >= last//2:
            return (1 << h) - 1
        return (1 << h) - 1 - (last//2)+curr

    def Solve(self,A):
        ncr = self.combination(A,A)
        dp=[0 for _ in range(A+1)]
        dp[0]=dp[1]=1
        for i in range(2,A+1):
            l = self.left_node(i)
            dp[i] = (ncr[i-1][l] * dp[l] * dp[i-1-l]) % self.mod
        return dp[A]

A=4
B=Solution()
print(B.Solve(A))
