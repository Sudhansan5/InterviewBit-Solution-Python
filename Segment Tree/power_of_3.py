class Solution:
    def build(self,A,B,s,e,node):
        if s==e:
            B[node]=int(A[s])
            return
        mid=(s+e)//2
        self.build(A,B,s,mid,2*node+1)
        self.build(A,B,mid+1,e,2*node+2)
        B[node]=B[2*node+1]+B[2*node+2]

    def update(self,A,B,s,e,node,i):
        if s==e:
            if A[i]==0:
                A[i]=1
                B[node]=1
            return
        mid=(s+e)//2
        if i > mid:
            self.update(A,B,mid+1,e,2*node+2,i)
        else:
            self.update(A,B,s,mid,2*node+1,i)
        B[node]=B[2*node+1]+B[2*node+2]

    def query(self,A,B,s,e,l,r,node):
        if s > r or e < l:
            return 0
        if s >= l and e <=r:
            return B[node]
        mid=(s+e)//2
        ans1=self.query(A,B,s,mid,l,r,2*node+1)
        ans2=self.query(A,B,mid+1,e,l,r,2*node+2)
        return ans1+ans2

    def Solve(self,A,B):
        n=len(A)
        arr1=[0 for _ in range(n)]
        arr2=[0 for _ in range(n)]
        for i in range(n):
            if i%2==0:
                arr1[i] = int(A[i])
            else:
                arr2[i] = int(A[i])
        C=[0 for _ in range(4*n)]
        D=[0 for _ in range(4*n)]
        self.build(arr1,C,0,n-1,0)
        self.build(arr2,D,0,n-1,0)
        ans=[]
        for i,j,k in B:
            if i==1:
                if (j-1)%2==0:
                    self.update(arr1,C,0,n-1,0,j-1)
                else:
                    self.update(arr2,D,0,n-1,0,j-1)
                ans.append(k)
            else:
                b=self.query(arr1,C,0,n-1,j-1,k-1,0)
                c=self.query(arr2,D,0,n-1,j-1,k-1,0)
                if (k-1)%2 == 0:
                    ans.append(((b - c) % 3 + 3) % 3)
                else:
                    ans.append(((c - b) % 3 + 3) % 3)
        return ans

A = '10010'
B =[[0, 3, 5],
    [0, 3, 4],
    [1, 2,-1],
    [0, 1, 5],
    [1, 2,-1],
    [0, 1, 4]]
C=Solution()
print(C.Solve(A,B))
