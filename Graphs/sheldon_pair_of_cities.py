class Solution:
    def Solve(self,A,B,C,D,E,F,G,H):
        graph=[[float('inf')]*A for _ in range(A)]
        ans=[]
        for i,j,k in zip(D,E,F):
            graph[i-1][j-1]=k
            graph[j-1][i-1]=k

        for k in range(A):
            for i in range(A):
                for j in range(A):
                    if i==j:
                        graph[i][j]=0
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
        for i in range(A):
            for j in range(A):
                if graph[i][j]==float('inf'):
                    graph[i][j]=-1
        for i,j in zip(G,H):
            ans.append(graph[i-1][j-1])
        return ans

A = 15
B = 18
C = 29
D = [ 11, 2, 2, 6, 2, 8, 9, 3, 14, 15, 4, 14, 8, 7, 8, 6, 2, 12 ]
E = [ 2, 1, 1, 2, 1, 1, 7, 3, 2, 13, 2, 1, 6, 1, 7, 1, 2, 10 ]
F = [ 8337, 6651, 29, 7765, 3428, 5213, 6431, 2864, 3137, 4024, 8169, 5013, 7375, 3786, 4326, 6415, 8982, 6864 ]
G = [ 6, 2, 1, 15, 12, 2, 14, 10, 13, 15, 15, 4, 8, 7, 9, 4, 15, 13, 12, 5, 2, 10, 1, 11, 14, 7, 3, 13, 12 ]
H = [ 5, 2, 15, 13, 6, 2, 8, 6, 3, 13, 15, 3, 1, 1, 4, 4, 5, 8, 1, 3, 1, 10, 15, 9, 2, 1, 1, 10, 2 ]
I=Solution()
print(I.Solve(A,B,C,D,E,F,G,H))
