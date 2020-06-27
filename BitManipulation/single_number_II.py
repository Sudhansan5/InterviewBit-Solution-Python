class Solution:
    def Solve(self,A):
        n = len(A)
        ans = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if A[j] & (1 << i):
                    count += 1
                    count %= 3
            if count != 0:
                ans |= count << i
        return ans


if __name__ == '__main__':
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    B = Solution()
    print(B.Solve(A))
