from collections import deque
from ordered_set import OrderedSet
class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, vis):
        vis[i][j] = True

        row = [-1, 0, 1, 0, -1, 1, -1, 1]
        col = [0, -1, 0, 1, -1, 1, 1, -1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 1 and not vis[nRow][nCol]:
                vis[nRow][nCol] = True
                self.dfs(A, nRow, nCol, vis)

    def solve(self,A):
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j] == 1:
                    self.dfs(A,i,j,vis)
                    count += 1

        return count



    def bfs(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False]*n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i,j))

        count = 0
        while q:
            i,j = q.popleft()

            if vis[i][j]: continue
            vis[i][j] = True

            row = [-1, 0, 1, 0, -1, 1, -1, 1]
            col = [0, -1, 0, 1, -1, 1, 1 ,-1]

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 1 and not vis[nRow][nCol]:
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))

            count += 1

        return count-1


if __name__ == '__main__':
    A = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

    B = Solution()
    print(B.bfs(A))
    print(B.solve(A))
