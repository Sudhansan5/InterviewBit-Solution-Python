from collections import deque
class Solution:
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if A[i][j]==2:
                    q.append((i,j,0))
        t=0
        while q:
            i,j,t=q.popleft()
            if i < m-1 and A[i+1][j]==1:
                A[i+1][j]=2
                q.append((i+1,j,t+1))

            if j < n-1 and A[i][j+1] == 1:
                A[i][j+1]=2
                q.append((i,j+1,t+1))

            if i > 0 and A[i-1][j] == 1:
                A[i-1][j]=2
                q.append((i-1,j,t+1))

            if j > 0 and A[i][j-1] == 1:
                A[i][j-1]=2
                q.append((i,j-1,t+1))

        lst=[1 in i for i in A]
        print(lst)
        return -1 if True in lst else t

A=[[2,1,1],[1,1,0],[0,1,1]]
B=Solution()
print(B.Solve(A))
