class Solution:
	# @param A : integer
	# @param B : list of list of integers
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
	        parent[C]=D
	        height[D]+=1

	def solve(self, A, B):
	    parent=[i for i in range(A)]
	    height=[0 for _ in range(A)]
	    B=sorted(B,key=lambda list: list[2])
	    mst_wt=0
	    for i,j,k in B:
	        C=self.find_root(i-1,parent)
	        D=self.find_root(j-1,parent)
	        if C!=D:
	            mst_wt+=k
	            self.Union(C,D,parent,height)
	    return mst_wt
	    
