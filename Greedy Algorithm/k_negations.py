from heapq import *
class Solution:
    def Solve(self,A,B):
        heapify(A)
        for _ in range(B):
            b=heappop(A)
            heappush(A,-b)
        return sum(A)

A = [24, -68, -29, -9, 84]
B = 4
C = Solution()
print(C.Solve(A,B))
