class DSU:
    def __init__(self,m):
        self.parent=[i for i in range(m+1)]
        self.height=[0 for _ in range(m+1)]
        self.ans=m

    def find_root(self,A):
        if self.parent[A]==A:
            return A
        return self.find_root(self.parent[A])

    def Union(self,A,B):
        C=self.find_root(A)
        D=self.find_root(B)
        if C==D:
            return
        if self.height[C] < self.height[D]:
            C,D = D,C
        self.parent[D]=C
        if self.height[C]==self.height[D]:
            self.height[C]+=1
        self.ans-=1

class Solution:
    def Solve(self,A):
        m=len(A)
        dsu=DSU(m)
        for i in range(m):
            if A[i] != 1:
                dsu.Union(i+1,A[i])
            else:
                dsu.ans-=1
        return dsu.ans


A=[1,2,1,2]
B=Solution()
print(B.Solve(A))
