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
        parent=[i for i in range(m)]
        height=[0 for _ in range(m)]
        vis=[False for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(1,m):
                k,l=A[i]
                o,n=A[j]
                vis[i]=True
                if (k==o or l==n) and not vis[j]:
                    self.Union(i,j,parent,height)
                    vis[j]=True
                    count+=1
        return count
