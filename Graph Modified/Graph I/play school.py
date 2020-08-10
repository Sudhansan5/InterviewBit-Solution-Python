class Solution:
    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'p':
                    q.append((i, j))
        level = 0
        while q:
            i, j = q.pop(0)
            vis[i][j] = True

            row = [1, 0, -1, 0]
            col = [0, 1, 0, -1]

            for r, c in zip(row, col):
                new_r = i + r
                new_c = j + c

                if new_r > m - 1 or new_r < 0 or new_c > n - 1 or new_c < 0:
                    continue

                vis[new_r][new_c] = True
                if A[new_r][new_c] == 'h':
                    level += 1

        return level


if __name__ == '__main__':
    A = [['.', '.', '.', 'p', 'h'],
         ['.', 'h', '.', '.', '.'],
         ['p', '.', 'p', 'h', '.']]

    B = Solution()
    print(B.Solve(A))
