class Solution:
    def countSetBits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def dp(self,A,B,mask,dp):
        index = self.countSetBits(mask)
        ans = 0

        if mask in dp:
            return dp[mask]

        for j in range(len(A)):
            if (mask >> j) & 1:
                continue
            ans = max(ans, A[index] ^ B[j] + self.dp(A,B,mask ^ (1<<j),dp))

        dp[mask] = ans
        return ans

    def Solve(self,A,B):
        dp = {}
        return self.dp(A,B,0,dp),dp


if __name__ == '__main__':
    A = [1, 0, 3]
    B = [5, 3, 4]
    C = Solution()
    print(C.Solve(A,B))
