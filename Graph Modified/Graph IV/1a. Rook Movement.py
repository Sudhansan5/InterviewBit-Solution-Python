from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def Solve(self, A, B, C, D, E):
        m = len(E)
        n = len(E[0])
        dis = [[float('inf')] * n for _ in range(m)]
        vis = [[False] * n for _ in range(m)]
        q = deque()
        q.append((A - 1, B - 1, 0))
        dis[A - 1][B - 1] = 0
        while q:
            i, j, k = q.popleft()
            vis[i][j] = True
            row = [1, 0, -1, 0]
            col = [0, 1, 0, -1]

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                while self.isValid(E, nRow, nCol) and E[nRow][nCol] == '0':
                    nRow += r
                    nCol += c

                if (dis[i][j] + 1) < dis[nRow - r][nCol - c]:
                    vis[nRow - r][nCol - c] = True
                    dis[nRow - r][nCol - c] = dis[i][j] + 1
                    q.append((nRow - r, nCol - c, k + 1))

        return dis[C - 1][D - 1] if dis[C - 1][D - 1] != float('inf') else -1


if __name__ == '__main__':
    # A = 1
    # B = 1
    # C = 4
    # D = 5
    # E = [['0','0', '0', '1', '0'],
    #      ['0', '0', '0', '1', '1'],
    #      ['1', '1', '0', '0', '0'],
    #      ['0', '1', '0', '0', '0']]

    A = 1
    B = 1
    C = 3
    D = 6

    E = ["0000000000", "0111111110", "0000100010", "0000100000", "0000000010", "0000100100", "0000100010", "0000100100",
         "0010001010", "1000101000"]

    F = Solution()
    print(F.Solve(A, B, C, D, E))
