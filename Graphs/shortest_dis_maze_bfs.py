from _collections import deque
class Solution:
    def Solve(self,A,B,C):
        m=len(A)
        n=len(A[0])
        dis=[[float('inf')]*n for _ in range(m)]
        dis[B[0]][B[1]]=0
        row=[1,0,-1,0]
        col=[0,1,0,-1]
        q=deque()
        q.append((B[0],B[1]))
        while q:
            i,j=q.popleft()
            for k in range(4):
                x = i + row[k]
                y = j + col[k]
                count = 0
                while x >= 0 and x < m and y >= 0 and y < n and A[x][y] == 0:
                    x += row[k]
                    y += col[k]
                    count += 1
                if dis[i][j] + count < dis[x-row[k]][y-col[k]]:
                    dis[x-row[k]][y-col[k]] = dis[i][j] + count
                    q.append((x-row[k],y-col[k]))

        return -1 if dis[C[0]][C[1]] == float('inf') else dis[C[0]][C[1]]
