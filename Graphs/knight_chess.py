from _collections import deque
class Solution:
    def __init__(self,m,n):
        self.graph=[[float('inf')]*n for _ in range(m)]

    def dfs(self,v,vis):
        vis[v]=True
        for i in self.graph[v]:
            if not vis[i]:
                self.dfs(i,vis)

    def Solve(self,A,B,C,D,E,F):
        row=[-2,-2,-1,-2,-1,1,2,2]
        col=[-1,1,1,2,-2,-2,-1,1]
        self.graph[C-1][D-1]=0
        q=deque()
        q.append((C-1,D-1,0))
        while q:
            x,y,t=q.popleft()

            for i in range(8):
                dx = x + row[i]
                dy = y + col[i]
                if dx >= 0 and dx < A and dy >= 0 and dy < B and 1+t < self.graph[dx][dy]:
                    self.graph[dx][dy] = 1+t
                    q.append((dx,dy,t+1))
        if self.graph[E-1][F-1]==float('inf'):
            return -1
        return self.graph[E-1][F-1]

A=8
B=8
C=1
D=1
E=8
F=8
G=Solution(A,B)
print(G.Solve(A,B,C,D,E,F))
