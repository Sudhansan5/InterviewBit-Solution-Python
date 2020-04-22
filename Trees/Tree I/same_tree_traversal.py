class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def check(self,A,B,C,n):
        if n==0:
            return 1
        if n==1:
            return A[0]==B[0] and B[0]==C[0]
        index=-1
        for i in range(n):
            if B[i]==A[0]:
                index=i
                break
        if index==-1:
            return 0
        ans1=self.check(A[1:],B,C,index)
        ans2=self.check(A[index+1:],B[index+1:],C[index:],n-index-1)
        return ans1 and ans2

    def Solve(self,A,B,C):
        m=len(A)
        n=len(B)
        o=len(C)
        if m==n and n==o:
            ans=self.check(A,B,C,m)
            if ans:
                return 1
            return 0
        return 0

A = [1, 2, 4, 5, 3]
B = [4, 2, 5, 1, 3]
C = [4, 5, 2, 3, 1]
D=Solution()
print(D.Solve(A,B,C))
