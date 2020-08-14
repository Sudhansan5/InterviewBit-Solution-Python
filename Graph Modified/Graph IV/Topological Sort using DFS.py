from collections import defaultdict


class Solution:
    def dfs(self, v, vis, stack):
        vis[v] = True
        for node in self.graph[v]:
            if not vis[node]:
                vis[node] = True
                self.dfs(node, vis, stack)
        stack.append(v)

    def Solve(self, A, B):
        vis = [False for _ in range(A)]
        stack = []
        self.graph = defaultdict(list)
        for i, j in B:
            self.graph[i].append(j)

        for i in range(A):
            if not vis[i]:
                vis[i] = True
                self.dfs(i, vis, stack)

        return stack[::-1]


if __name__ == '__main__':
    A = 4
    B = [[0, 1],
         [0, 2],
         [1, 3],
         [2, 1],
         [2, 3]]
    C = Solution()
    print(C.Solve(A, B))
