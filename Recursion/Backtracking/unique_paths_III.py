class Solution:
    def isValid(self,A,u,v):
        return 0 <= u and\
               u < len(A) and\
               0 <= v and\
               v < len(A[0]) and\
               A[u][v] != -1

    def dfs(self,A,x,y,count):
        if A[x][y] == 2:
            if count == 0:
                return 1
            return 0

        A[x][y] = -1
        ans = 0
        for i in range(4):
            u = x + self.row[i]
            v = y + self.col[i]
            if self.isValid(A,u,v):
                ans += self.dfs(A,u,v,count-1)

        A[x][y] = 0
        return ans

    def Solve(self,A):
        self.row = [1,0,0,-1]
        self.col = [0,1,-1,0]
        u, v = -1, -1
        count = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    u = i
                    v = j
                elif A[i][j] == 0:
                    count += 1

        return self.dfs(A,u,v,count+1)


if __name__ == '__main__':
    A = [[1, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 2, -1]]
    B = Solution()
    print(B.Solve(A))
