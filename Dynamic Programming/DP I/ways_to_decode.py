class Solution:
    def dp(self,A,n,aux):
        if aux[n]:
            return aux[n]
        if n==0:
            return 1
        s = len(A)-n
        if A[s] == '0':
            return 0
        ans = self.dp(A,n-1,aux)
        if n >= 2 and int(A[s:s+2]) <= 26:
            ans += self.dp(A,n-2,aux)
        aux[n] = ans
        return ans

    def Solve(self,A):
        n=len(A)
        aux=[0 for _ in range(n+1)]
        self.dp(A,n,aux)
        return aux[n]

A="121"
B=Solution()
print(B.Solve(A))
