class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
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

    def solve(self, A, B):
        parent=[i for i in range(A)]
        height=[0 for _ in range(A)]
        ans=[]
        for i,j,k in B:
            if i==0:
                self.Union(j-1,k-1,parent,height)
            elif i==1:
                x=self.find_root(j-1,parent)
                y=self.find_root(k-1,parent)
                if x==y:
                    ans.append(1)
                else:
                    ans.append(0)
        return ans
        
