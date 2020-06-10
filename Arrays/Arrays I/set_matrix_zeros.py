class Solution:
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        r1, c1 = 0, 0
        for i in range(n):
            if A[0][i] == 0:
                r1=1
                break

        for i in range(m):
            if A[i][0] == 0:
                c1=1
                break

        for i in range(1,m):
            for j in range(1,n):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0

        if r1:
            for i in range(n):
                A[0][i] = 0
        if c1:
            for i in range(m):
                A[i][0] = 0
        return A


if __name__ == '__main__':
    A=[[1, 0, 1],
       [1, 1, 1],
       [1, 1, 1]]
    B=Solution()
    print(B.Solve(A))
