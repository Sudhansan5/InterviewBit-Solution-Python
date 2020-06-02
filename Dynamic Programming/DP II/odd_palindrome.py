class Solution:
    def dp(self,A,i,j,n,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i < 0 or j >= n:
            return 1
        if i == 0 and j == n-1:
            if A[i] == A[j]:
                ans = 2
            else:
                ans = 1
            aux[i][j] = ans
            return ans

        if A[i] == A[j]:
            ans = self.dp(A,i-1,j,n,aux) + self.dp(A,i,j+1,n,aux)
        else:
            ans = self.dp(A,i-1,j,n,aux) + self.dp(A,i,j+1,n,aux) - self.dp(A,i-1,j+1,n,aux)
        aux[i][j] = ans
        return ans

    def Solve(self,A):
        mod=1000000007
        n=len(A)
        dp=[[0]*(n+1) for _ in range(n+1)]
        ans=[0]*n
        for i in range(n):
            if i == 0 or i == n-1:
                ans[i] = 1
            else:
                count = self.dp(A,i-1,i+1,n,dp)
                ans[i] = count%mod
        return ans

    def isPalindrome(self,A):
        mod=1000000007
        n=len(A)
        dp=[[0]*(n+1) for _ in range(n)]
        for l in reversed(range(n)):
            for i in range(n):
                j=i+l
                if j >= n:
                    break
                if i==0 and j == n-1:
                    if A[i] == A[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    if A[i] == A[j]:
                        if i > 0:
                            dp[i][j] += dp[i-1][j]
                        if j < n-1:
                            dp[i][j] += dp[i][j+1]
                        if i <= 0 or j >= n-1:
                            dp[i][j] += 1
                    else:
                        if i > 0:
                            dp[i][j] += dp[i-1][j]
                        if j < n-1:
                            dp[i][j] += dp[i][j+1]
                        if i > 0 and j < n-1:
                            dp[i][j] -= dp[i-1][j+1]
        ans=[]
        for i in range(n):
            if i == 0 or i == n-1:
                ans.append(1)
            else:
                ans.append(dp[i-1][i+1]%mod)
        return ans

A = "ababzz"
B = Solution()
print(B.Solve(A))
print(B.isPalindrome(A))
