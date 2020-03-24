from _collections import defaultdict
import heapq
class Graph:
    def __init__(self,m):
        self.graph=defaultdict(list)
        self.vis=[False for _ in range(m)]
        self.dis=[float('inf') for _ in range(m)]

    def add_edge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def remove_edge(self,u,v,w):
        self.graph[u].remove((v,w))
        self.graph[v].remove((u,w))

    def shortest_path(self,u,v):
        pq=[]
        heapq.heappush(pq,(u,0))
        self.dis[u]=0
        while pq:
            node,distance=heapq.heappop(pq)
            self.vis[node]=True
            for j,k in self.graph[node]:
                new_dis=distance+k
                if new_dis < self.dis[j]:
                    self.dis[j]=new_dis
                    heapq.heappush(pq,(j,new_dis))
        return self.dis[v]

    def find_min(self,B):
        min_cycle = float('inf')
        for i,j in enumerate(self.graph):
            for k in self.graph[j]:
                l,m = k
                print(l,m)
                self.remove_edge(j,l,m)
                dist = self.shortest_path(j,l)
                min_cycle = min(min_cycle,dist+m)
        # for i,j,k in B:
        #     self.remove_edge(i-1,j-1,k)
        #     dist = self.shortest_path(i-1,j-1)
        #     min_cycle = min(min_cycle,dist+k)
        #     self.add_edge(i-1,j-1,k)
        return min_cycle

class Solution:
    def Solve(self,A,B):
        graph = Graph(A)
        for i,j,k in B:
            graph.add_edge(i-1,j-1,k)
        return graph.find_min(B)

A = 4
B = [[1 ,2 ,2],
     [2 ,3 ,3],
     [3 ,4 ,1],
     [4 ,1 ,4],
     [1 ,3 ,15]]
C=Solution()
print(C.Solve(A,B))
