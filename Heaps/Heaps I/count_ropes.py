import heapq
class Solution:
    def Solve(self,A):
        heapq.heapify(A)
        ans=0
        while len(A) > 1:
            a=heapq.heappop(A)
            b=heapq.heappop(A)
            ans+=(a+b)
            heapq.heappush(A,a+b)
        return ans

A=[1,2,3,4,5]
B=Solution()
print(B.Solve(A))
