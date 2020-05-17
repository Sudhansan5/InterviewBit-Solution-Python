from heapq import heappop, heappush
class Solution:
    def Solve(self,A):
        n=len(A)
        min_heap=[]
        max_heap=[]
        ans=[]
        for i in range(n):
            if len(min_heap)==len(max_heap):
                heappush(max_heap,-A[i])
                heappush(min_heap,-heappop(max_heap))
            else:
                heappush(min_heap,A[i])
                heappush(max_heap,-heappop(min_heap))

            if len(min_heap) >= len(max_heap):
                b=heappop(min_heap)
                ans.append(b)
                heappush(min_heap,b)
            else:
                b=heappop(max_heap)
                ans.append(-b)
                heappush(max_heap,b)
        return ans

A=[1,2,5,4,3]
B=Solution()
print(B.Solve(A))
