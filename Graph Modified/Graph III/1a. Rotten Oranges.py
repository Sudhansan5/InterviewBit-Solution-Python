class Solution:
    def find_root(self, A, parent):
        if parent[A] == A:
            return A
        return self.find_root(parent[A], parent)

    def union(self, A, B, parent, height):
        C = self.find_root(A, parent)
        D = self.find_root(B, parent)

        if C == D:
            return

        if height[C] < height[D]:
            parent[C] = D
        elif height[C] > height[D]:
            parent[D] = C
        else:
            parent[D] = C
            height[C] += 1

    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        parent = [i for i in range(m * n)]
        height = [0 for _ in range(m * n)]

        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]

        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 2:
                    for r, c in zip(row, col):
                        nRow = i + r
                        nCol = j + c
                        if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 1:
                            A[nRow][nCol] = 2
                            C = self.find_root(i * n + j, parent)
                            D = self.find_root(nRow * n + nCol, parent)

                            if C == D:
                                continue
                            count += 1
                            self.union(C, D, parent, height)

        return count, A, parent


if __name__ == '__main__':
    A = [
        [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
        [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
        [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
        [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
        [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
        [2, 2, 0, 2, 2, 1, 1, 1, 2, 2]
    ]

    B = Solution()
    print(B.Solve(A))
