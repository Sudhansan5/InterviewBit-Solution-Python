class Solution:
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    A[i][j]=1
                elif A[i][j]==1:
                    A[i][j]=0
                elif i==0 or j==0:
                    if i==0:
                        A[i][j]=A[i][j-1]
                    else:
                        A[i][j]=A[i-1][j]
                else:
                    A[i][j]=A[i][j-1]+A[i-1][j]
        return A[-1][-1]

A = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
B=Solution()
print(B.Solve(A))
