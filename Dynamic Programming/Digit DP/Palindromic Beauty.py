class Solution:
    def isPalindrome(self,A):
        return A == A[::-1]

    def dp(self,A,n,pos,flag,palindrome, dp):
        if pos == n:
            return 1

        lim = 9 if flag else A[pos]
        ans = 0

        for i in range(lim+1):
            ans += self.dp(A,n,pos+1, 1 if i < A[pos] else flag,
                           1 if self.isPalindrome(A) else palindrome, dp)

        return ans

    def Solve(self,A):
        mod = pow(10, 9) + 7
        n = len(A)
        ans = []
        for i in range(n // 2):
            dp = {}

            start = str(int(A[2 * i]) - 1)
            start = [int(i) for i in start]

            end = A[2 * i + 1]
            end = [int(i) for i in end]

            h = self.dp(end, len(end), 0, 0, 0, dp)
            dp.clear()
            l = self.dp(start, len(start), 0, 0, 0, dp)
            ans.append((h - l))
            print(h,l)

        return ans

if __name__ == '__main__':
    A = ["1", "5", "7", "12"]
    B = Solution()
    print(B.Solve(A))
