class Solution:
    def Solve(self,A):
        ans = 0
        for i in A:
            ans ^= i
        return ans

if __name__ == '__main__':
    A = [1, 2, 2, 3, 1]
    B = Solution()
    print(B.Solve(A))
