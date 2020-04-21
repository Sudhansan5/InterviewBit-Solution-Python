class Solution:
    def update(self,tree,lazy,s,e,node,l,r,val):
        if lazy[node] != 0:
            tree[node] += (e-s+1) * lazy[node]
            if s != e:
                lazy[2*node+1] = lazy[node]
                lazy[2*node+2] = lazy[node]
            lazy[node] = 0

        if s > e or s > r or e < l:
            return

        if s >= l and e <= r:
            tree[node] += (e-s+1) * val
            if s != e:
                lazy[2*node+1] += val
                lazy[2*node+2] += val
            return

        mid=(s+e)//2
        self.update(tree,lazy,s,mid,2*node+1,l,r,val)
        self.update(tree,lazy,mid+1,e,2*node+2,l,r,val)
        tree[node]=tree[2*node+1]+tree[2*node+2]

    def query(self,tree,lazy,s,e,node,l,r):
        if s > e or s > r or e < l:
            return 0

        if lazy[node] != 0:
            tree[node] += (e-s+1)*lazy[node]
            if s != e:
                lazy[2*node+1] = lazy[node]
                lazy[2*node+2] = lazy[node]
            lazy[node] = 0

        if s >= l and e <= r:
            return tree[node]

        mid=(s+e)//2
        ans1=self.update(tree,lazy,s,mid,2*node+1,l,r)
        ans2=self.update(tree,lazy,mid+1,e,2*node+2,l,r)
        return ans1+ans2

    def Solve(self,A,B):
        arr=['0' for _ in range(A)]
        return

A=5
B=[[0, 1, 3],
   [1, 1, 2],
   [0, 0, 4],
   [1, 3, 4]]
C=Solution()
print(C.Solve(A,B))
