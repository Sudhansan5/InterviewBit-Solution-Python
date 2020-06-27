class Solution:
    def Solve(self,A):
        n=len(A)
        A.sort()
        min_xor = float('inf')
        for i in range(n-1):
            min_xor = min(min_xor,A[i]^A[i+1])
        return min_xor

if __name__ == '__main__':
    A = [0, 2, 5, 7]
    B = Solution()
    print(B.Solve(A))
