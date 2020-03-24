from _collections import defaultdict
import heapq
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def remove_edge(self,u,v,w):
        self.graph[u].remove((v,w))
        self.graph[v].remove((u,w))

    def shortest_dis(self,A,B,u,v):
        dis=[float('inf')]*A
        vis=[False]*A
        pq=[]
        heapq.heappush(pq,(u,0))
        dis[u]=0
        while pq:
            node,distance = heapq.heappop(pq)
            vis[node]=True
            for j,k in self.graph[node]:
                new_dis = distance + k
                if new_dis < dis[j]:
                    dis[j] = new_dis
                    heapq.heappush(pq,(j,new_dis))
        return dis[v]

    def find_min_cycle(self,A,B):
        min_cycle=float('inf')
        for i,j,k in B:
            self.remove_edge(i-1,j-1,k)
            dist = self.shortest_dis(A,B,i-1,j-1)
            min_cycle = min(min_cycle,dist + k)
        return min_cycle

class Solution:
    def Solve(self,A,B):
        graph = Graph()
        for i,j,k in B:
            graph.add_edge(i-1,j-1,k)
        return graph.find_min_cycle(A,B)

A = 4
B = [[1 ,2 ,2],
     [2 ,3 ,3],
     [3 ,4 ,1],
     [4 ,1 ,4],
     [1 ,3 ,15]]
C=Solution()
print(C.Solve(A,B))
