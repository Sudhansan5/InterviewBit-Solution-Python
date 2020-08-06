class Solution:
    def Solve(self,A):
        n = len(A)
        ans = 1
        i = 1
        while i < n-1:
            ans += A[i-1] * A[i] * A[i+1]
            #A.pop(i)
            i += 1


        return ans

if __name__ == '__main__':
    A = [1, 2, 4, 3]
    B = Solution()
    print(B.Solve(A))
