from collections import defaultdict


class Solution:
    def dfs(self, v, vis):
        vis[v] = True
        self.cnt += 1
        for node in self.graph[v]:
            if not vis[node]:
                vis[node] = True
                self.dfs(node, vis)

    def Solve(self, A, B):
        m = len(B)
        n = len(B[0])
        self.graph = defaultdict(list)

        for i in range(m):
            for j in range(n):
                if B[i][j] == 1:
                    self.graph[i].append(j)
        ans = 0
        for i in range(A):
            vis = [False for _ in range(A)]
            self.cnt = 0
            self.dfs(i, vis)
            if self.cnt == A:
                ans += 1

        return ans


if __name__ == '__main__':
    A = 4
    B = [[0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]

    D = [[0, 0, 0, 0, 1, 1],
         [1, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0]]

    C = Solution()
    print(C.Solve(A, D))
