from math import sqrt
class Solution:
    def Solve(self,A):
        n=int(sqrt(A))
        ans=[]
        for i in range(2,n+1):
            while A%i == 0:
                A //= i
                ans.append(i)
        if A != 1:
            ans.append(A)
        return ans

if __name__ == '__main__':
    A=14
    B=Solution()
    print(B.Solve(A))
