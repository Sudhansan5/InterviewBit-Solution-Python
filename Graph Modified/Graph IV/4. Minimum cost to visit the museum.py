from collections import defaultdict, deque
from heapq import *


class Solution:
    def Solve(self, A, B, C, D):
        n = len(A)
        graph = defaultdict(list)

        for i, j, k in zip(B, C, D):
            graph[i - 1].append((j - 1, k))
            graph[j - 1].append((i - 1, k))

        # pq = []
        # for i in range(n):
        #     pq.append((A[i], i))
        #     heapify(pq)
        #     vis = [False for _ in range(n)]
        #     dis = [float('inf') for _ in range(n)]
        #     dis[i] = A[i]
        #     while pq:
        #         w, v = heappop(pq)
        #         vis[v] = True
        #         for node, wt in graph[v]:
        #             new_wt = w + wt
        #             if new_wt < dis[node]:
        #                 dis[node] = new_wt
        #                 heappush(pq, (new_wt, node))
        #
        #     print(dis)


        ans = []
        for i in range(n):
            q = []
            vis = [False for _ in range(n)]
            dis = [float('inf') for _ in range(n)]
            #q.append((i,A[i]))
            heappush(q, (A[i], i))
            dis[i] = A[i]

            while q:
                size = len(q)
                for i in range(size):
                    w, v = heappop(q)
                    vis[v] = True
                    for node, wt in graph[v]:
                        new_wt = w + wt
                        if new_wt < dis[node]:
                            dis[node] = new_wt
                            heappush(q,(A[node], node))

            ans.append(dis[i])
            print(dis)

        return ans


if __name__ == '__main__':
    A = [31, 99, 5, 26, 74, 83, 15]
    B = [1, 1, 7, 6, 2, 2, 4, 2, 4, 5, 1]
    C = [5, 4, 4, 3, 2, 6, 4, 7, 5, 6, 2]
    D = [42, 30, 33, 21, 48, 39, 39, 15, 50, 42, 1]
    E = Solution()
    print(E.Solve(A, B, C, D))
