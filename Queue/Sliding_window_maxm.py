from collections import deque
class Solution:
    def Solve(self,A,B):
        q=deque()
        ans=[]
        for i,j in enumerate(A):
            while q and q[-1][1] < j:
                q.pop()
            q.append((i,j))
            if i >= B-1:
                if q[0][0] < i-B+1:
                    q.popleft()
                ans.append(q[0][1])
        return ans

A=[1,3,-1,-3,5,3,6,7]
B=3
C=Solution()
print(C.Solve(A,B))
