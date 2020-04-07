from collections import deque
class Solution:
    def Solve(self,A):
        A+=[0]
        m=len(A)
        stack=deque()
        stack.append(-1)
        ans=float('-inf')
        for i in range(m):
            while stack and A[stack[-1]] > A[i]:
                h = stack.pop()
                ans = max(ans,(i-stack[-1]-1)*A[h])
            stack.append(i)
        return 0 if ans == float('-inf') else ans

A=[4,1,2,4,5,1,3]
B=Solution()
print(B.Solve(A))
