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

    def Solve(self,A):
        n=len(A)
        ans=set()
        for i in range(n):
            for j in range(i,n):
                ans.add(self.gcd(A[i],A[j]))
        return len(ans)

if __name__ == '__main__':
    A=[3,2,8]
    B=Solution()
    print(B.Solve(A))
