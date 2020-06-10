class Solution:
    def Solve(self,A,B,C,D,E):
        m=len(A)
        n=len(A[0])
        mod=1000000007
        for i in range(1,m):
            for j in range(n):
                A[i][j] += A[i-1][j]
                if A[i][j] < 0:
                    A[i][j] += mod
                A[i][j] %= mod

        for i in range(m):
            for j in range(1,n):
                A[i][j] += A[i][j-1]
                if A[i][j] < 0:
                    A[i][j] += mod

        q=len(B)
        ans=[0 for _ in range(q)]
        for i in range(q):
            top=B[i]-1
            left=C[i]-1
            bottom=D[i]-1
            right=E[i]-1
            ans[i] = A[bottom][right]
            ans[i] %= mod

            if top:
                ans[i] -= A[top-1][right]
                ans[i] %= mod

            if left:
                ans[i] -= A[bottom][left-1]
                ans[i] %= mod

            if top and left:
                ans[i] += A[top-1][left-1]
                ans[i] %= mod

        return ans

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [1, 2]
    C = [1, 2]
    D = [2, 3]
    E = [2, 3]
    F=Solution()
    print(F.Solve(A,B,C,D,E))
