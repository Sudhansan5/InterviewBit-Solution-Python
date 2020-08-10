from collections import deque
class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False]*n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 0
                    q.append((i,j))
                else:
                    A[i][j] = -1

        while q:
            i,j = q.popleft()
            vis[i][j] = True
            row = [0,1,0,-1]
            col = [1,0,-1,0]

            for r,c in zip(row,col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A,nRow,nCol) and not vis[nRow][nCol] and A[nRow][nCol] != A[i][j]:
                    A[nRow][nCol] = A[i][j] + 1
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))

        return A

if __name__ == '__main__':
    A = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 0]]

    B = Solution()
    print(B.Solve(A))
