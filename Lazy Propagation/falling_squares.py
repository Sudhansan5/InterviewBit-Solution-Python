class Solution:
    def query(self,l,r,height):
        return max(height[i] for i in range(l,r+1))

    def update(Self,l,r,height,h):
        for i in range(l,r+1):
            height[i]=max(height[i],h)

    def Solve(self,A):
        #co-ordinate compression
        cords=set()
        for l,s in A:
            r=l+s-1
            cords.add(l)
            cords.add(r)
        index={x: i for i,x in enumerate(sorted(cords))}
        height=[0]*len(index)
        best=0
        ans=[]
        for left, size in A:
            l=index[left]
            r=index[left+size-1]
            h=self.query(l,r,height)+size
            self.update(l,r,height,h)
            best=max(best,h)
            ans.append(best)
        return ans

A = [[1, 2], [2, 3], [6, 1]]
B=Solution()
print(B.Solve(A))
