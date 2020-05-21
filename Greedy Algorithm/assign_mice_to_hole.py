from heapq import *
class Solution:
    def Solve(self,A,B):
        heapify(A)
        heapify(B)
        ans=[]
        while A and B:
            b=heappop(A)
            c=heappop(B)
            ans.append(abs(b-c))
        return max(ans)


A = [-4, 2, 3]
B = [0, -2, 4]
C=Solution()
print(C.Solve(A,B))
