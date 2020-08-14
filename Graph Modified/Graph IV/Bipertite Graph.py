from collections import deque


class Solution:
    def isValid(self, A, v, color, colors):
        if colors[v] != 0: return colors[v] == color
        colors[v] = color
        for node in A[v]:
                if not self.isValid(A, node, -color, colors):
                    return False
        return True

    def Solve(self, A):
        n = len(A)
        colors = [0 for _ in range(n+1)]
        for i in range(n):
            if colors[i] == 0 and not self.isValid(A, i, 1, colors):
                    return False
        return True

    def bfs(self, A):
        n = len(A)
        colors = [0 for _ in range(n)]
        q = deque()

        for i in range(n):
            if colors[i] != 0: continue
            q.append((i, 1))

            while q:
                curr, color = q.popleft()
                colors[curr] = color

                for node in A[curr]:
                    if colors[node] == 0:
                        colors[node] = -color
                        q.append((node, -color))

                    elif colors[node] == colors[curr]:
                        return False

        return True

if __name__ == '__main__':
    A = [[0, 1],
         [0, 2],
         [1, 3],
         [1, 2],
         [2, 3],
         [3, 4]]

    C = [[1,2,3],
         [0,2],
         [0,1,3],
         [0,2]]

    D = [[1],
         [0,3],
         [3],
         [1,2]]

    B = Solution()
    print(B.Solve(D))
    print(B.bfs(D))
