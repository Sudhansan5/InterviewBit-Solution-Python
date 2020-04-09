from collections import deque
class Solution:
    def Solve(self,A,B):
        A.sort()
        q=deque()
        ans=[]
        for i in A:
            q.append(i)
        while q:
            b=q.popleft()
            ans.append(b)
            if len(ans)==B:
                break
            for i in A:
                c = str(b)+str(i)
                q.append(int(c))
        return ans

A=[1,2,3,4]
B=10
C=Solution()
print(C.Solve(A,Ba))
