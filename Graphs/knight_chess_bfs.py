from _collections import deque
class Solution:
    def __init__(self,A,B):
        self.graph=[[0]*B for _ in range(A)]
        self.vis=[[False]*B for _ in range(A)]

    def dfs(self,v,vis):
        vis[v]=True
        for i in self.graph[v]:
            if not vis[i]:
                self.dfs(i,vis)

    def Solve(self,A,B,C,D,E,F):
        q=deque()
        q.append((C-1,D-1,0))
        t=0
        while q:
            i,j,t=q.popleft()
            self.vis[i][j]=True
            if i > 1 and j > 0 and not self.vis[i-2][j-1]:
                self.graph[i-2][j-1]=t+1
                q.append((i-2,j-1,t+1))
            if i > 1 and j < B-1 and not self.vis[i-2][j+1]:
                self.graph[i-2][j+1]=t+1
                q.append((i-2,j+1,t+1))
            if i > 0 and j > 1 and not self.vis[i-1][j-2]:
                self.graph[i-1][j-2]=t+1
                q.append((i-1,j-2,t+1))
            if i > 0 and j < B-2 and not self.vis[i-1][j+2]:
                self.graph[i-1][j+2]=t+1
                q.append((i-1,j+2,t+1))
            if i < A-1 and j > 1 and not self.vis[i+1][j-2]:
                self.graph[i+1][j-2]=t+1
                q.append((i+1,j-2,t+1))
            if i < A-1 and j < B-2 and not self.vis[i+1][j+2]:
                self.graph[i+1][j+2]=t+1
                q.append((i+1,j+2,t+1))
            if i < A-2 and j > 0 and not self.vis[i+2][j-1]:
                self.graph[i+2][j-1]=t+1
                q.append((i+2,j-1,t+1))
            if i < A-2 and j < B-1 and not self.vis[i+2][j+1]:
                self.graph[i+2][j+1]=t+1
                q.append((i+2,j+1,t+1))

        return t,self.graph[E-1][F-1]

A = 4
B = 7
C = 2
D = 6
E = 2
F = 4
G=Solution(A,B)
print(G.Solve(A,B,C,D,E,F))
