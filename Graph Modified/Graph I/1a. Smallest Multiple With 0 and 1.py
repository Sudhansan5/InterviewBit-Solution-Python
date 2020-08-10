class Solution:
    def dp(self,n, size):
        bit = 1 << size - 1
        global ans
        while bit:
            ans = 1 if n & bit else 0
            bit >>= 1
        return ans

    def Solve(self, A):
        for i in range(1,10):
            a = self.dp(i,5)
            print(a)


if __name__ == '__main__':
    A = 55
    B = Solution()
    print(B.Solve(A))
