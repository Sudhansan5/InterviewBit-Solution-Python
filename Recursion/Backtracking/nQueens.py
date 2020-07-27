class Solution:
    def nQueens(self, n, row, placed):
        if row >= n:
            return True

        for col in range(n):
            if self.colV[col] or self.leftD[row + col] or self.rightD[row - col + n]:
                continue
            placed[row] = col

            self.colV[col] = 1
            self.leftD[row + col] = 1
            self.rightD[row - col + n] = 1

            if self.nQueens(n, row + 1, placed):
                return True

            self.colV[col] = 0
            self.leftD[row + col] = 0
            self.rightD[row - col + n] = 0

        return False

    def Solve(self, A):
        self.colV = [0 for _ in range(A)]
        self.leftD = [0 for _ in range(2 * A)]
        self.rightD = [0 for _ in range(2 * A)]
        placed = [-1 for _ in range(A)]
        self.nQueens(A, 0, placed)
        ans = [placed]
        result = []

        if A == 1:
            return [['Q']]
        else:
            ans.append([A - placed[i] - 1 for i in range(A)])

        for i in ans:
            res = [['.'] * A for _ in range(A)]
            for j, k in enumerate(i):
                res[j][k] = 'Q'
            result.append(["".join(i) for i in res])

        return result


if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.Solve(A))
