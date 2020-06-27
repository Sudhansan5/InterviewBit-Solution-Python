class Solution:
    def Solve(self, A):
        ans = 0
        if A > 0:
            while A:
                r = A % 10
                ans = ans * 10 + r
                A //= 10
        else:
            A = abs(A)
            while A:
                r = A % 10
                ans = ans * 10 + r
                A //= 10
            ans = int("-" + str(ans))

        if abs(ans) > 2 ** 31:
            return 0
        return ans


if __name__ == '__main__':
    A = 123
    B = Solution()
    print(B.Solve(A))
