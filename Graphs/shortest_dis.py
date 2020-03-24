from _collections import defaultdict
import heapq
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    def Solve(self,A,B,C,D):
        dis=[float('inf')]*A
        vis=[False]*A
        for i,j,k in B:
            self.graph[i].append((j,k))
            self.graph[j].append((i,k))
        pq=[]
        heapq.heappush(pq,(C,0))
        dis[C]=0
        while pq:
            node,distance = heapq.heappop(pq)
            vis[node]=True
            for j,k in self.graph[node]:
                new_dis=distance+k
                if new_dis < dis[j]:
                    dis[j]=new_dis
                    heapq.heappush(pq,(j,new_dis))
        return dis[D]

A = 6
B = [   [2, 5, 1],
        [1, 3, 1] ,
        [0, 5, 2] ,
        [0, 2, 2] ,
        [1, 4, 1] ,
        [0, 1, 1] ]
C = 3
D = 2
E=Solution()
print(E.Solve(A,B,C,D))
