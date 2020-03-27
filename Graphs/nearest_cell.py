from _collections import deque
class Solution:
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        ans=[[float('inf')]*n for _ in range(m)]
        row=[1,0,-1,0]
        col=[0,1,0,-1]
        q=deque()
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    ans[i][j]=0
                    q.append((i,j))
        while q:
            i,j=q.popleft()
            for k in range(4):
                x=i+row[k]
                y=j+col[k]
                if x >= 0 and x < m and y >= 0 and y < n and ans[x][y] > ans[i][j]+1:
                    ans[x][y]=ans[i][j]+1
                    q.append((x,y))
        return ans

A = [[0, 0, 0, 1],
     [0, 0, 1, 1],
     [0, 1, 1, 0]]
B=Solution()
print(B.Solve(A))
