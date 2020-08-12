from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def floydWarshall(self, A, B, C, D, E, F, G, H):
        graph = [[float('inf')]*A for _ in range(A)]

        for i,j,k in zip(D,E,F):
            graph[i-1][j-1] = k
            graph[j-1][i-1] = k

        for i in range(A):
            graph[i][i] = 0

        for k in range(A):
            for i in range(A):
                for j in range(A):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for i in range(A):
            for j in range(A):
                if graph[i][j] == float('inf'):
                    graph[i][j] = -1

        ans = []
        for i,j in zip(G,H):
            ans.append(graph[i-1][j-1])

        return graph, ans

    def Solve(self, A, B, C, D, E, F, G, H):
        graph = defaultdict(list)

        for i,j,k in zip(D,E,F):
            graph[i-1].append((j-1,k))
            graph[j-1].append((i-1,k))

        ans = []
        for s,e in zip(G,H):
            vis = [False for _ in range(A)]
            dis = [float('inf') for _ in range(A)]
            dis[s-1] = 0

            pq = []
            heappush(pq, (0, s-1))

            while pq:
                dist, node = heappop(pq)
                vis[node] = True
                for v,w in graph[node]:
                    new_dist = dist + w
                    if new_dist < dis[v]:
                        dis[v] = new_dist
                        heappush(pq, (new_dist, v))

            ans.append(dis[e-1])
        return ans


if __name__ == '__main__':
    A = 4
    B = 6
    C = 2
    D = [1, 2, 3, 2, 4, 3]
    E = [2, 3, 4, 4, 1, 1]
    F = [4, 1, 1, 1, 1, 1]
    G = [1, 1]
    H = [2, 3]
    I = Solution()
    print(I.Solve(A, B, C, D, E, F, G, H))
    print(I.floydWarshall(A,B,C,D,E,F,G,H))
