class Solution:
    def update(self,tree,lazy,s,e,node,l,r):
        if lazy[node] != 0:
            tree[node] = (e-s+1) - tree[node]
            if s != e:
                lazy[2*node+1] ^= 1
                lazy[2*node+2] ^= 1
            lazy[node] = 0

        if s > e or s > l or e < l:
            return

        if s >= l and e <= r:
            tree[node] = (e-s+1) - tree[node]
            if s != e:
                lazy[2*node+1] ^= 1
                lazy[2*node+2] ^= 1
            return

        mid=(s+e)//2
        self.update(tree,lazy,s,mid,2*node+1,l,r)
        self.update(tree,lazy,mid+1,e,2*node+2,l,r)
        tree[node] = tree[2*node+1] + tree[2*node+2]

    def query(self,tree,lazy,s,e,node,l,r):
        if s > e or s > r or e < l:
            return 0

        if lazy[node] != 0:
            tree[node] = (e-s+1) - tree[node]
            if s != e:
                lazy[2*node+1] ^= 1
                lazy[2*node+2] ^= 1
            lazy[node] = 0

        if s >= l and e <= r:
            return tree[node]

        mid=(s+e)//2
        ans1=self.query(tree,lazy,s,mid,2*node+1,l,r)
        ans2=self.query(tree,lazy,mid+1,e,2*node+2,l,r)
        return ans1+ans2

    def Solve(self,A,B):
        tree=[0 for _ in range(4*A)]
        lazy=[0 for _ in range(4*A)]
        ans=0
        for i,j,k in B:
            if i==0:
                self.update(tree,lazy,0,A-1,0,j,k)
            else:
                b=self.query(tree,lazy,0,A-1,0,j,k)
                ans+=b
        return ans

A = 7
B = [[0, 3, 5],
     [0, 0, 5],
     [0, 0, 6],
     [1, 6, 6],
     [1, 1, 6]]
C=Solution()
print(C.Solve(A,B))
