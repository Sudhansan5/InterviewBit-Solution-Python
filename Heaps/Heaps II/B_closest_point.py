from heapq import heappop, heappush
from math import sqrt
class Solution:
    def Solve(self,A,B):
        min_heap=[]
        for i,j in A:
            dis=sqrt(i**2 + j**2)
            heappush(min_heap,(dis,i,j))
        ans=[]
        for _ in range(B):
            i,j,k=heappop(min_heap)
            ans.append([j,k])
        return ans

A=[[1,3],[-2,2]]
B=1
C=Solution()
print(C.Solve(A,B))
