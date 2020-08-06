class Solution:
    def dp(self, A, n, pos, flag, digit_sum):
        if pos == n:
            return digit_sum == 0

        lim = 9 if flag else A[pos]
        ans = 0
        for i in range(lim+1):
            ans += self.dp(A,n,pos+1,(1 if i < A[pos] else flag), (digit_sum + i %3))

        return ans


    def Solve(self,A):
        n = len(A)
        return self.dp(A,n,0,0,0)

if __name__ == '__main__':
    A = [1,2,3]
    B = Solution()
    print(B.Solve(A))
