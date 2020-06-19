from math import sqrt
class Solution:
    def isPrime(self,A):
        if A < 2:
            return False
        n=int(sqrt(A))
        for i in range(2,n+1):
            if A%i==0:
                return False
        return True

    def Solve(self,A):
        prime=[True for _ in range(A)]
        ans=[]
        for i in range(2,A):
            if self.isPrime(i):
                for j in range(i,A):
                    if j*i < A:
                        prime[j*i]=False
                ans.append(i)
        return ans


if __name__ == '__main__':
    A=30
    B=Solution()
    print(B.Solve(A))
