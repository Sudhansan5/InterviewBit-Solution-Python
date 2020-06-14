class Solution:
    def gcd(self,A,B):
        if A == 0:
            return B
        elif B == 0:
            return A
        elif A == 1 or B == 1:
            return 1
        else:
            return self.gcd(B%A,A)

    def Solve(self,A,B,C):
        lcm = (B*C) // self.gcd(B,C)
        return A // lcm

if __name__ == '__main__':
    A=81991
    B=2549
    C=7
    D=Solution()
    print(D.Solve(A,B,C))
