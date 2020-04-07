from collections import deque
class Solution:
    def histogram(self,A):
        A+=[0]
        m=len(A)
        stack=deque()
        stack.append(-1)
        ans = float('-inf')
        for i in range(m):
            while stack and A[stack[-1]] > A[i]:
                h=stack.pop()
                ans=max(ans,(i-stack[-1]-1)*A[h])
            stack.append(i)
        return 0 if ans == float('-inf') else ans

    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    q.append((i,j))
        while q:
            i,j = q.popleft()
            if i < m-1 and A[i+1][j]==1:
                A[i+1][j]=A[i][j]+A[i+1][j]
                q.append((i+1,j))
        ans=float('-inf')
        for i in A:
            b=self.histogram(i)
            ans=max(ans,b)
        return 0 if ans == float('-inf') else ans

A = [[0, 0, 1],
     [0, 1, 1],
     [1, 1, 1]]
B=Solution()
print(B.Solve(A))
