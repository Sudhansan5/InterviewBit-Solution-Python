from collections import deque
class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def Solve(self, A, B, C, D, E, F):
        if E > A or F > B: return -1
        graph = [[float('inf')]*B for _ in range(A)]
        row = [-1, 1, -2, 2, -2, 2, -1, 1]
        col = [-2, -2, -1, -1, 1, 1, 2, 2]

        q = deque()
        q.append((C-1,D-1, 0))
        graph[C-1][D-1] = 0
        while q:
            i,j,t = q.popleft()

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isValid(graph,nRow, nCol) and graph[nRow][nCol] == float('inf'):
                    graph[nRow][nCol] = t + 1
                    q.append((nRow, nCol, t+1))

        return graph[E-1][F-1] if graph[E-1][F-1] != float('inf') else -1

if __name__ == '__main__':
    A = 2
    B = 4
    C = 2
    D = 1
    E = 4
    F = 4
    G = Solution()
    print(G.Solve(A, B, C, D, E, F))
