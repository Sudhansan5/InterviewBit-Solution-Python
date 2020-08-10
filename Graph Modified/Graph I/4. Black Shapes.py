class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self,A,i,j,vis):
        vis[i][j] = True
        row = [0,1,0,-1]
        col = [1,0,-1,0]

        for r,c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A,nRow, nCol) and not vis[nRow][nCol] and A[nRow][nCol] == 'X':
                vis[nRow][nCol] = True
                self.dfs(A,nRow,nCol,vis)

    def Solve(self,A):
        m = len(A)
        n = len(A[0])
        vis = [[False]*n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'O':
                    self.dfs(A,i,j,vis)
                    count += 1

        return count



if __name__ == '__main__':
    A = [['X', 'O'], ['O', 'X']]
    B = Solution()
    print(B.Solve(A))
