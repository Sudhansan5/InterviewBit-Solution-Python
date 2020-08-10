from collections import deque


class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def Solve(self, A, B, C):
        m = len(A)
        n = len(A[0])
        self.count = 0
        vis = [[False] * n for _ in range(m)]
        dis = [[float('inf')] * n for _ in range(m)]
        q = deque()
        q.append((B[0], B[1]))
        dis[B[0]][B[1]] = 0

        while q:
            i, j = q.popleft()
            vis[i][j] = True

            row = [1, 0, -1, 0]
            col = [0, 1, 0, -1]
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                count = 0

                while self.isValid(A, nRow, nCol) and A[nRow][nCol] == 0:
                    nRow += r
                    nCol += c
                    count += 1

                if dis[i][j] + count < dis[nRow - r][nCol - c]:
                    dis[nRow - r][nCol - c] = dis[i][j] + count
                    q.append((nRow - r, nCol - c))

        return dis[C[0]][C[1]] if dis[C[0]][C[1]] != float('inf') else -1, dis


if __name__ == '__main__':
    A = [[0, 0], [0, 1]]
    B = [0, 0]
    C = [0, 1]
    D = Solution()
    print(D.Solve(A, B, C))
