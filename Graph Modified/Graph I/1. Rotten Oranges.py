from collections import deque
class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False]*n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if A[i][j] == 2:
                    q.append((i,j, 0))

        count = 0
        while q:
            i,j, count = q.popleft()
            vis[i][j] = True
            row = [0,1,0,-1]
            col = [1,0,-1,0]

            for r,c in zip(row,col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A,nRow,nCol) and A[nRow][nCol] == 1 and not vis[nRow][nCol]:
                    A[nRow][nCol] = 2
                    vis[nRow][nCol] = True
                    q.append((nRow,nCol, count+1))

        lst=[1 in i for i in A]
        return -1 if True in lst else count

if __name__ == '__main__':
    A = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]

    B = Solution()
    print(B.solve(A))
