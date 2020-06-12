class Solution:
    def Solve(self,A):
        n=len(A)
        ans=0
        for i in range(n):
            for j in range(n):
                no_TL = (i+1)*(j+1)
                no_TR = (n-i)*(n-j)
                ans += no_TL * no_TR * A[i][j]
        return ans

if __name__ == '__main__':
    A=[[1, 1],
       [1, 1]]
    B=Solution()
    print(B.Solve(A))
