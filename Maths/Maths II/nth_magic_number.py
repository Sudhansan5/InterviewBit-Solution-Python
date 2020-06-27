class Solution:
    def Solve(self, A):
        power = 1
        ans = 0
        while A:
            power *= 5
            if A%2 == 1:
                ans += power

            A //= 2
        return ans

    def solve(self,A):
        power = 1
        ans =0
        while A:
            power *= 5
            if A & 1:
                ans += power
            A >>= 1
        return ans


if __name__ == '__main__':
    A = 5
    B = Solution()
    print(B.Solve(A))
    print(B.solve(A))
