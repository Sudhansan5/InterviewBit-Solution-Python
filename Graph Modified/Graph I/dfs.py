from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def dfs(self, v,vis):
        vis.add(v)
        for i in self.graph[v]:
            if not vis[i]:
                vis.add(i)
                self.dfs(i,vis)

    def Solve(self,A):
        return

if __name__ == '__main__':
    A = []
    B = Solution()
    print(B.Solve(A))
