class Solution:
    def Solve(self,A):
        mod=10003
        if A <= 2:
            return A
        if A == 3:
            return 4
        l=2
        r=4
        ans=0
        for i in range(4,A+1):
            ans = (r + (i-1)*l)%mod
            l=r
            r=ans
        return ans

A = 5
B = Solution()
print(B.Solve(A))
