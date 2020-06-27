class Solution:
    def Solve(self, A):
        divisor = 1
        while A / divisor >= 10:
            divisor *= 10

        while A:
            leading = A // divisor
            trailing = A % 10

            if leading != trailing:
                return 0

            # Removing the leading and
            # trailing digit from number
            A = (A % divisor) // 10

            # Reducing divisor by a factor
            # of 2 as 2 digits are dropped
            divisor //= 100

        return 1


if __name__ == '__main__':
    A = 12121
    B = Solution()
    print(B.Solve(A))
