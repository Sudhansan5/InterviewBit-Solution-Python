import sys
sys.setrecursionlimit(10**6)

class Solution:
    def catalan(self,A,dp):#memoization
        mod=1000000007
        if dp[A]:
            return dp[A]

        if A <= 1:
            dp[A]=1
            return dp[A]

        ans=0
        for i in range(A):
            ans += (self.catalan(i,dp) * self.catalan(A-i-1,dp))%mod
        dp[A]=ans%mod
        return ans%mod

    def Solve(self,A):
        dp=[0 for _ in range(A)]
        self.catalan(A-1,dp)
        return dp[-1]

    def solve(self,A):#Tabulation
        mod=1000000007
        dp=[0 for _ in range(A)]
        dp[0]=1
        dp[1]=1
        for i in range(2,A):
            for j in range(i):
                dp[i] += (dp[j] * dp[i-j-1])%mod
        return dp[-1]%mod

if __name__ == '__main__':
    A=5
    B=Solution()
    print(B.Solve(A))
    print(B.solve(A))
