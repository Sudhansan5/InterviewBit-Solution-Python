class Solution:
    def dp(self,A):
        n=len(A)
        dp = [0]*(n+1)
        for i in range(n):
            dp[i] = max(dp[i-1],dp[i-2]+A[i])
        return dp[n-1]

    def Solve(self,A):
        n=len(A[0])
        tmp=[]
        for i in range(n):
            tmp.append(max(A[0][i],A[1][i]))
        return self.dp(tmp)

A=[[1,2,3,4,5],
   [2,3,4,5,6]]
B=Solution()
print(B.Solve(A))
