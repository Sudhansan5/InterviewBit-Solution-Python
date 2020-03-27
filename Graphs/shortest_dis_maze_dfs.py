class Solution:
    def dfs(self,A,B,dis):
        m=len(A)
        n=len(A[0])
        row=[1,0,-1,0]
        col=[0,1,0,-1]
        for i in range(4):
            x=B[0]+row[i]
            y=B[1]+col[i]
            count=0
            while x >= 0 and x < m and y >= 0 and y < n and A[x][y] == 0:
                x += row[i]
                y += col[i]
                count += 1
            if dis[B[0]][B[1]]+count < dis[x-row[i]][y-col[i]]:
                dis[x-row[i]][y-col[i]] = dis[B[0]][B[1]]+count
                self.dfs(A,[x-row[i],y-col[i]],dis)

    def Solve(self,A,B,C):
        m=len(A)
        n=len(A[0])
        dis=[[float('inf')]*n for _ in range(m)]
        dis[B[0]][B[1]]=0
        self.dfs(A,B,dis)
        return -1 if dis[C[0]][C[1]] == float('inf') else dis[C[0]][C[1]]

A =[[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]]

B = [0, 4]
C = [4, 4]
D=Solution()
print(D.Solve(A,B,C))
