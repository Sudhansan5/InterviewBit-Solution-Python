from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[-1]*n for _ in range(m)]
        dis = [[0]*n for _ in range(m)]
        cnt = [[0]*n for _ in range(m)]
        q = deque()
        building_cnt = 0
        for k in range(m):
            for l in range(n):
                if A[k][l] == 1:
                    building_cnt += 1
                    q.append((k, l, 0))
                    vis[k][l] = building_cnt
                    level = 1
                    while q:
                        size = len(q)
                        for _ in range(size):
                            i, j, t = q.popleft()
                            row = [1, 0, -1, 0]
                            col = [0, 1, 0, -1]

                            for r, c in zip(row, col):
                                nRow = i + r
                                nCol = j + c

                                if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 0 and vis[nRow][nCol] != building_cnt:
                                    dis[nRow][nCol] += level
                                    cnt[nRow][nCol] += 1
                                    vis[nRow][nCol] = building_cnt
                                    q.append((nRow, nCol, t + 1))

                        level += 1
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0 and cnt[i][j] == building_cnt:
                    ans = min(ans, dis[i][j])

        return ans, dis


if __name__ == '__main__':
    A = [[1, 0, 2, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0]]

    B = Solution()
    print(B.Solve(A))
