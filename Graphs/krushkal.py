class Solution:
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

    def Krushkal(self,A,B):
        parent=[i for i in range(A)]
        height=[0 for _ in range(A)]
        mst_wt=0
        B=sorted(B,key=lambda item: item[2])
        result=[]
        for i,j,k in B:
            C=self.find_root(i-1,parent)
            D=self.find_root(j-1,parent)
            if C != D:
                result.append([i-1,j-1,k])
                mst_wt+=k
                self.Union(C,D,parent,height)
        return mst_wt

A = 4
B = [[1,2,1],
     [2,3,4],
     [1,4,3],
     [4,3,2],
     [1,3,10]]
C=Solution()
print(C.Krushkal(A,B))
