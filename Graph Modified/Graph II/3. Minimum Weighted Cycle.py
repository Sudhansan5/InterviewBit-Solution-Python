from collections import defaultdict
from heapq import *


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def removeEdge(self, u, v, w):
        self.graph[u].remove((v, w))
        self.graph[v].remove((u, w))

    def dijkstra(self, A, u, v):
        vis = [False for _ in range(A)]
        dis = [float('inf') for _ in range(A)]
        pq = []
        heappush(pq, (0, u))
        dis[u] = 0

        while pq:
            dist, node = heappop(pq)
            vis[node] = True
            for i, wt in self.graph[node]:
                new_dis = dist + wt
                if new_dis < dis[i]:
                    dis[i] = new_dis
                    heappush(pq, (new_dis, i))

        return dis[v]

    def min_cycle(self, A, B):
        min_cycle = float('inf')
        for i, j, k in B:
            self.removeEdge(i - 1, j - 1, k)
            dist = self.dijkstra(A, i - 1, j - 1)
            min_cycle = min(min_cycle, dist + k)

        return min_cycle


class Solution:
    def cycle(self, A, B, C):
        self.graph = defaultdict(list)

        for i, j, k in B:
            self.graph[i - 1].append((j - 1, k))
            self.graph[j - 1].append((i - 1, k))

        vis = [False for _ in range(A)]
        dis = [float('inf') for _ in range(A)]

        pq = []
        heappush(pq, (0, C))

        while pq:
            dist, node = heappop(pq)
            print(dist, node)
            for v, w in self.graph[node]:
                new_wt = dist + w
                if new_wt < dis[v]:
                    dis[v] = new_wt
                    vis[v] = True
                    heappush(pq, (new_wt, v))

        return dis, vis

    def Solve(self, A, B):
        graph = Graph()
        for i, j, k in B:
            graph.addEdge(i - 1, j - 1, k)

        return graph.min_cycle(A, B)


if __name__ == '__main__':
    A = 5
    B = [[1, 2, 1],
         [1, 5, 2],
         [5, 4, 3],
         [4, 3, 1],
         [3, 2, 5],
         [2, 5, 8],
         [5, 3, 6]]

    C = Solution()
    print(C.Solve(A, B))
