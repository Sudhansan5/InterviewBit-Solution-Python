class Solution:
    def isSafe(self,i,j,vis,m,n,graph):
        if i>=0 and i<m and j>=0 and j<n and not vis[i][j] and graph[i][j]=='X':
            return True
        return False
    def dfs(self,i,j,vis,m,n,graph):
        row=[1,0,-1,0]
        col=[0,1,0,-1]
        vis[i][j]=True
        for k in range(len(row)):
            if self.isSafe(i+row[k],j+col[k],vis,m,n,graph):
                self.dfs(i+row[k],j+col[k],vis,m,n,graph)
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        vis=[[False]*n for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j]=='X':
                    self.dfs(i,j,vis,m,n,A)
                    count+=1
        return count

A=[['O','O','O','X','O','O','O'],
   ['O','O','X','X','O','X','O'],
   ['O','X','O','O','O','X','O']]
C=[['X','X','X'],
   ['X','X','X'],
   ['X','X','X']]
B=Solution()
print(B.Solve(A))
