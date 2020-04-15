class Solution:
    def count(self,n):
        count=0
        while n:
            count+= n&1
            n>>=1
        return count

    def update(self,A,B,s,e,node,i,val):
        if s==e:
            A[i]=val
            B[node]=val
            return
        mid=(s+e)//2
        if i > mid:
            self.update(A,B,mid+1,e,2*node+2,i,self.count(2*A[i]+1))
        else:
            self.update(A,B,s,mid,2*node+1,i,self.count(2*A[i]+1))
        B[node]=B[2*node+1]+B[2*node+2]

    def update1(self,A,B,s,e,node,i,val):
        if s==e:
            A[i]=val
            B[node]=val
            return
        mid=(s+e)//2
        if i > mid:
            self.update(A,B,mid+1,e,2*node+2,i,self.count(A[i]//2))
        else:
            self.update(A,B,s,mid,2*node+1,i,self.count(A[i]//2))
        B[node]=B[2*node+1]+B[2*node+2]

    def query(self,A,B,s,e,l,r,node):
        if s > r or e < l:
            return 0
        if s >= l and e <= r:
            return B[node]

        mid=(s+e)//2
        ans1=self.query(A,B,s,mid,l,r,2*node+1)
        ans2=self.query(A,B,mid+1,e,l,r,2*node+2)
        return ans1+ans2

    def Solve(self,A,B):
        arr=[0 for _ in range(A)]
        ans=[0 for _ in range(4*A)]
        res=[]
        for i,j,k in B:
            if i==1:
                self.update(arr,ans,0,A-1,0,j-1,j-1)
            elif i==2:
                self.update1(arr,ans,0,A-1,0,j-1,j-1)
            else:
                b=self.query(arr,ans,0,A-1,j-1,k-1,0)
                res.append(b)
        return res

A = 5
B =[[1, 1,-1],
    [1, 2,-1],
    [1, 3,-1],
    [3, 1, 3],
    [3, 2, 4]]
D=[[1, 1, -1],
   [1, 2, -1],
   [3, 1, 3],
   [2, 1, -1],
   [3, 1, 3] ]
C=Solution()
print(C.Solve(A,B))
