from collections import defaultdict


class Solution:
    def dfs(self, u, vis):
        vis[u] = 1

        for v in self.graph[u]:
            if v not in vis:
                vis[v] = 1
                self.dfs(v,vis)


    def Solve(self, A, B, C):
        n = len(A)
        self.graph = defaultdict(list)
        for i,j in enumerate(A):
            self.graph[j].append(i+1)

        vis = [0 for _ in range(n+1)]
        self.dfs(C, vis)

        return vis[B]

if __name__ == '__main__':
    A = [1, 1, 2]
    B = 1
    C = 2
    D = Solution()
    print(D.Solve(A, B, C))
