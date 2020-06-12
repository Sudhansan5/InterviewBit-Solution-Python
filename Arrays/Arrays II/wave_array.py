class Solution:
    def Solve(self,A):
        A.sort()
        n=len(A)
        for i in range(0,n-1,2):
            for j in range(i+1,n):
                if A[i] <= A[j]:
                    A[i],A[j] = A[j],A[i]
                break
        return A


if __name__ == '__main__':
    A=[5, 1, 3, 2, 4]
    B=Solution()
    print(B.Solve(A))
