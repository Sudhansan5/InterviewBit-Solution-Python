class Solution:
    def Solve(self,A):
        n=len(A)
        mod=1000000007
        ans = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if A[j] & (1 << i):
                    count += 1
            ans += count * (n-count) * 2
        return ans%mod

if __name__ == '__main__':
    A = [1, 3, 5]
    B = Solution()
    print(B.Solve(A))
