from math import sqrt
class Solution:
    def Solve(self,A):
        n=int(sqrt(A))
        ans=[0]*n
        for i in range(1,n):
            if A%i == 0:
                ans[i] = i
                ans[n-i] = A//i

        for i in ans:
            if i == 0:
                ans.remove(i)
        return ans

if __name__ == '__main__':
    A=100
    B=Solution()
    print(B.Solve(A))
