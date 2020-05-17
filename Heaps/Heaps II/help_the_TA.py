from heapq import heappop, heappush
class Solution:
    def Solve(self,A,B):
        n=len(A)
        max_heap=[]
        for i in range(n):
            heappush(max_heap,(-A[i],i))
        ans=[]
        for i in range(B):
            j,k=heappop(max_heap)
            if j==0:
                break
            ans.append(k)
            heappush(max_heap,(j+1,k))
        return ans

A=[2,10,5,1,1]
B=46
C=Solution()
print(C.Solve(A,B))
