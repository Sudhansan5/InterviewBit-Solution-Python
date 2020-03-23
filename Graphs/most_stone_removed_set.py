class Solution:
    # @param A : list of list of integers
    # @return an integer
    def find_root(self,A,parent):
        if parent[A]==A:
            return A
        return self.find_root(parent[A],parent)

    def Union(self,A,B,parent,height):
        C=self.find_root(A,parent)
        D=self.find_root(B,parent)
        if C==D:
            return
        if height[C]<height[D]:
            parent[C]=D
        elif height[C]>height[D]:
            parent[D]=C
        else:
            parent[D]=C
            height[C]+=1

    def solve(self, A):
        m=len(A)
        parent=[i for i in range(20000)]
        height=[0 for _ in range(20000)]
        count=0
        for i in range(m):
            self.Union(A[i][0],A[i][1]+10000,parent,height)
        ans=set()
        for i in range(m):
            ans.add(self.find_root(A[i][0],parent))
        return m-len(ans)

A =[[0, 0],
    [0, 1],
    [1, 0],
    [1, 2],
    [2, 2],
    [2, 1]]
B=Solution()
print(B.solve(A))
