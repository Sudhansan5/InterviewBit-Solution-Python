class Solution:
    def Solve(self,A):
        m=len(A)
        dis=[float('inf')]*m
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if A[i][j]==-1:
                        A[i][j]=float('inf')
                    A[i][j]=min(A[i][j],A[i][k]+A[k][j])
                    dis[i]=A[i][j]
        return dis.index(max(dis))+1

A = [[0, 6, 8, -1],
     [6, 0, 9, -1],
     [8, 9, 0, 4],
     [-1, -1, 4, 0]]
C=[[0, 8, 8, -1],
  [8, 0, 4, -1],
  [8, 4, 0, 1],
  [-1, -1, 1, 0]]
B=Solution()
print(B.Solve(A))
