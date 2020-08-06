class Solution:
    def isPalindrome(self,s,i,j):
        return s[i:j+1] == s[i:j+1][::-1]

    def dp(self,s,index,dp):
        if self.isPalindrome(s,index, len(s)-1):
            return 0

        if index in dp:
            return dp[index]

        ans = float('inf')
        for i in range(index, len(s)+1):
            print(s[index:i])
            if self.isPalindrome(s,index,i):
                ans = min(ans, 1 + self.dp(s,i+1,dp))

        dp[index] = ans
        return ans

    def Solve(self,A):
        n = len(A)
        dp = {}
        if self.isPalindrome(A,0,n-1):
            return 0
        return self.dp(A,0,dp), dp

    def minCut(self, s):
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]

        ans = float('inf')
        for i in range(1, n+1):
            for j in range(i):
                if self.isPalindrome(s,i,j):
                    ans = min(ans, 1 + dp[i][j])


if __name__ == '__main__':
    A = 'abba'
    B = Solution()
    print(B.Solve(A))
