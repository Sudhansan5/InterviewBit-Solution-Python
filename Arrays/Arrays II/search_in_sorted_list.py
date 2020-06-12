class Solution:
    def Solve(self,A):
        m=len(A)
        n=len(A[0])
        q=[]
        for i in range(m):
            for j in reversed(range(n)):
                q.append((i,j))
                break
            break
        while q:
            i,j=q.pop()
            if B < A[i][j] and j > 0:
                q.append((i,j-1))
            if B > A[i][j] and i < m-1:
                q.append((i+1,j))
            if A[i][j] == B:
                return (i+1)*1009+(j+1)
        return -1

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = 2
    C=Solution()
    print(C.Solve(A))
