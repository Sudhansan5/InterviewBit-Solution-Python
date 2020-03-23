from _collections import defaultdict
import heapq
class Solution:
    def Solve(self,A,B,C):
        graph=defaultdict(list)
        for i,j,k in B:
            graph[i].append((j,k))
            graph[j].append((i,k))
        vis=[False]*A
        dis=[float('inf')]*A
        dis[C]=0
        pq=[]
        heapq.heappush(pq,(C,0))
        while pq:
            node,distance=heapq.heappop(pq)
            vis[node]=True
            for v in graph[node]:
                new_dis=distance+v[1]
                if new_dis < dis[v[0]]:
                    dis[v[0]]=new_dis
                    heapq.heappush(pq,(v[0],new_dis))
        return dis

A=6
B =[[0, 4, 9],
    [3, 4, 6],
    [1, 2, 1],
    [2, 5, 1],
    [2, 4, 5],
    [0, 3, 7],
    [0, 1, 1],
    [4, 5, 7],
    [0, 5, 1]]
C=4
E=[[0, 3, 4],
   [2, 3, 3],
   [0, 1, 9],
   [3, 4, 10],
   [1, 3, 8]]
D=Solution()
print(D.Solve(A,B,C))
