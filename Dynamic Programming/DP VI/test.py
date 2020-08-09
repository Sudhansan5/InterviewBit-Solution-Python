class Solution:
    def Solve(self, A):
        n = len(A)
        i = 0
        j = 0

        count = 0
        while i < n or j < n:
            if A[i] == '1':
                count += 1
                j += 1
            i += 1

        return count



if __name__ == '__main__':
    A = '011010100000100'
    B = Solution()
    print(B.Solve(A))
