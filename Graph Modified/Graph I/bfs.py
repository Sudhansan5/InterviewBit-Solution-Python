from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u ,v):
        return self.graph[u].append(v)

    def bfs(self,s):
        n = len(self.graph)
        vis = [False for _ in range(n)]
        vis[s] = True
        q = []
        q.append(s)
        while q:
            node = q.pop(0)
            print(node, end=' --> ')
            for i in self.graph[node]:
                if not vis[i]:
                    vis[i] = True
                    q.append(i)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.bfs(2)
