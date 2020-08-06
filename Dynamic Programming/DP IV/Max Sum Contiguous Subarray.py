class Solution:
    def Solve(self,A):
        n = len(A)
        maxx = A[0]
        curr_max = A[0]

        for i in range(1,n):
            curr_max = max(curr_max + A[i], A[i])
            maxx = max(curr_max,maxx)

        return maxx

if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    B = Solution()
    print(B.Solve(A))
