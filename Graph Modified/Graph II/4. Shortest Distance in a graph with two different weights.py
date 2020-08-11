from collections import defaultdict
from heapq import *

class Solution:
    def Solve(self, A, B, C, D):
        graph = defaultdict(list)

        for i,j,k in B:
            graph[i].append((j,k))
            graph[j].append((i,k))

        vis = [False for _ in range(A)]
        dis = [float('inf') for _ in range(A)]
        pq = []
        heappush(pq,(0,C))
        dis[C] = 0

        while pq:
            dist, node = heappop(pq)
            vis[node] = True

            for v,w in graph[node]:
                new_wt = dist +  w
                if new_wt < dis[v]:
                    dis[v] = new_wt
                    heappush(pq, (new_wt, v))

        return dis[D] if dis[D] != float('inf') else -1

if __name__ == '__main__':
    A = 6
    B = [[2, 5, 1],
         [1, 3, 1],
         [0, 5, 2],
         [0, 2, 2],
         [1, 4, 1],
         [0, 1, 1]]
    C = 3
    D = 2
    E = Solution()
    print(E.Solve(A, B, C, D))
