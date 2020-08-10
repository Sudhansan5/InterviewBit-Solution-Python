from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        return self.graph[u].append((v, w))

    def shortestPathToDest(self, s, d, k, v):
        vis = [False for _ in range(v)]
        dis = [float('inf') for _ in range(v)]
        q = [[] for _ in range(k * v)]

        dis[s] = 0
        q[0].append(s)

        for i in range(k * v):
            while q[i]:
                curr_node = q[i].pop(0)
                vis[curr_node] = True

                for node in self.graph[curr_node]:
                    if not vis[node[0]] and dis[node[0]] > dis[curr_node] + node[1]:
                        dis[node[0]] = dis[curr_node] + node[1]
                        q[i + node[1]].append(node[0])
                        vis[node[0]] = True

        return dis

    def Solve(self):
        v = len(self.graph)
        return self.shortestPathToDest(0, 2, 2, v)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 2)
    g.addEdge(0, 3, 2)
    g.addEdge(1, 0, 1)
    g.addEdge(1, 3, 2)
    g.addEdge(2, 0, 2)
    g.addEdge(2, 4, 1)
    g.addEdge(2, 5, 1)
    g.addEdge(3, 1, 2)
    g.addEdge(3, 0, 2)
    g.addEdge(4, 2, 1)
    g.addEdge(5, 2, 1)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 5, 2)
    print(g.Solve())
