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

    def Solve(self, A):
        n = len(A)
        parent = [i for i in range(20000)]
        height = [0 for _ in range(20000)]

        for i in range(n):
            self.union(A[i][0],A[i][1]+10000,parent,height)

        ans = set()
        for i in range(n):
            ans.add(self.find_root(A[i][0], parent))

        return n - len(ans)



if __name__ == '__main__':
    A = [[0, 0],
         [0, 1],
         [1, 0],
         [1, 2],
         [2, 2],
         [2, 1]]

    B = Solution()
    print(B.Solve(A))
