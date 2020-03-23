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
        if height[C] < height[D]:
            parent[C]=D
        elif height[C] > height[D]:
            parent[D]=C
        else:
            parent[D]=C
            height[C]+=1

    def solve(self,A):
        m=len(A)
        n=len(A[0])
        parent=[i for i in range((m*n))]
        height=[0]*(m*n)
        count=0
        for i in range(m):
            for j in range(n):
                if A[i][j]==0:
                    continue
                if i<m-1 and A[i+1][j]==1:
                    self.Union(i*n+j,(i+1)*n+j,parent,height)
                    count+=1
                if j<n-1 and A[i][j+1]==1:
                    self.Union(i*n+j,i*n+(j+1),parent,height)
                    count+=1
                if i > 0 and A[i-1][j]==1:
                    self.Union(i*n+j,(i-1)*n+j,parent,height)
                    count+=1
                if j > 0 and A[i][j-1]==1:
                    self.Union(i*n+j,i*n+(j-1),parent,height)
                    count+=1
                if i < m-1 and j<n-1 and A[i+1][j+1]==1:
                    self.Union(i*n+j,(i+1)*n+(j+1),parent,height)
                    count+=1
                if i > 0 and j>0 and A[i-1][j-1]==1:
                    self.Union(i*n+j,(i-1)*n+(j-1),parent,height)
                    count+=1
                if i<m-1 and j>0 and A[i+1][j-1]==1:
                    self.Union(i*n+j,(i+1)*n+(j-1),parent,height)
                    count+=1
                if i>0 and j<n-1 and A[i-1][j+1]==1:
                    self.Union(i*n+j,(i-1)*n+(j+1),parent,height)
                    count+=1
        c=[0]*(m*n)
        cout=0
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    x=self.find_root(i*n+j,parent)
                    if c[x]==0:
                        cout+=1
                        c[x]+=1
                    else:
                        c[x]+=1
        return cout
