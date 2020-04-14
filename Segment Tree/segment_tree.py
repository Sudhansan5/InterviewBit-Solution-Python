class Solution:
    def build(self,A,B,s,e,node):
        if s==e:
            B[node]=A[s]
            return
        mid = (s+e)//2
        self.build(A,B,s,mid,2*node+1)
        self.build(A,B,mid+1,e,2*node+2)
        B[node]=B[2*node+1]+B[2*node+2]

    def update(self,A,B,s,e,node,i,val):
        if s==e:
            A[i]=val
            B[node]=val
            return

        mid=(s+e)//2
        if i > mid:
            self.update(A,B,mid+1,e,2*node+2,i,val)
        else:
            self.update(A,B,s,mid,2*node+1,i,val)
        B[node] = B[2*node+1]+B[2*node+2]

    def query(self,A,B,s,e,node,l,r):
        if s > r or e < l:
            return 0
        if s >= l and e <= r:
            return B[node]
        mid = (s+e)//2
        ans1 = self.query(A,B,s,mid,2*node+1,l,r)
        ans2 = self.query(A,B,mid+1,e,2*node+2,l,r)
        return ans1+ans2

    def Solve(self,A):
        n=len(A)
        B=[0]*(4*n)
        self.build(A,B,0,n-1,0)
        self.update(A,B,0,n-1,0,2,3)
        self.query(A,B,0,n-1,0,2,3)
        return B

A=[2,3,1,7,6,-1,3]
B=Solution()
print(B.Solve(A))
