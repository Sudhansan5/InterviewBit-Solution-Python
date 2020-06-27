class Solution:
    def Solve(self,A,B):
        INT_MAX = pow(2,31) - 1
        INT_MIN = -(pow(2,31) - 1)
        n=abs(A)
        m=abs(B)
        sign = -1 if n < 0 ^ m < 0 else 1
        q=0
        t=0
        for i in range(31,-1,-1):
            if t + (m << i) <= n:
                t += m << i
                q |= 1 << i
        if sign < 0:
            q = -q

        return INT_MAX if q < INT_MIN or q >= INT_MAX else q


if __name__ == '__main__':
    A=-2147483648
    B=-10000000
    C=Solution()
    print(C.Solve(A,B))
