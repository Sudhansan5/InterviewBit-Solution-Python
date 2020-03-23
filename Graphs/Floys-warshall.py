class Solution:
    def Solve(self,A):
        m=len(A)
        dis=[float('inf')]*m
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if A[i][j] == -1:
                        A[i][j] = float('inf')
                    A[i][j]=min(A[i][j],A[i][k]+A[k][j])
                    dis[i] = A[i][j]

        for i in range(m):
            for j in range(m):
                if A[i][j]==float('inf'):
                    A[i][j]=-1
        return dis

A=[
  [0, 5, -1, 10],
  [-1, 0, 3, -1],
  [-1, -1, 0, 1],
  [-1, -1, -1, 0]
]
B=Solution()
print(B.Solve(A))
