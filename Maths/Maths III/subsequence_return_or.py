from math import gcd
class Solution:
    def Solve(self,A):
        n=len(A)
        gcd_ = gcd(A[0],A[1])
        for i in range(2,n):
            gcd_ = gcd(gcd_,A[i])
        if gcd_ == 1:
            return 1
        return 0

if __name__ == '__main__':
    A=[1, 2, 3]
    B=Solution()
    print(B.Solve(A))
