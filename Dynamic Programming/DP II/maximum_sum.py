class Solution:
    def Solve(self,A,B,C,D):
        n=len(A)
        l=[0 for _ in range(n)]
        l[0] = A[0]*B
        for i in range(1,n):
            l[i] = max(l[i-1],A[i]*B)
        r=[0 for _ in range(n)]
        r[n-1] = A[n-1]*D
        for i in reversed(range(n-1)):
            r[i] = max(r[i+1],A[i]*D)
        ans=float('-inf')
        for i in range(n):
            ans = max(ans, l[i]+A[i]*C+r[i])
        return ans

A = [1, 5, -3, 4, -2]
B = 2
C = 1
D = -1
E=Solution()
print(E.Solve(A,B,C,D))
