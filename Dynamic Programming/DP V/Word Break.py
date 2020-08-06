class Solution:
    def dp(self, s, dic, dp):  # Top-Down
        if s == "":
            return 1

        if s in dic:
            return 1

        if s in dp:
            return dp[s]

        for i in range(1, len(s) + 1):
            if s[:i] in dic and self.dp(s[i:], dic, dp):
                print(s[:i])
                dp[s] = 1
                return dp[s]

        dp[s] = 0
        return dp[s]


    def Solve(self,A,B):
        dp = {}
        return self.dp(A,B,dp)

    def wordBreak(self, A, B):
        n = len(A)
        dp = [0 for _ in range(n+1)]

        for i in range(1,n+1):
            if not dp[i] and A[:i] in B:
                dp[i] = 1

            if dp[i] == 1:
                if i == n:
                    dp[i] = 1
                else:
                    for j in range(i+1,n+1):
                        if not dp[j] and A[i:j] in B:
                            dp[j] = 1

                        if j == n and dp[j]:
                            dp[j] = 1

        return dp[-1]

if __name__ == '__main__':
    A = "myinterviewtrainer"
    B = ["trainer", "my", "interview"]
    C = Solution()
    print(C.Solve(A,B))
    print(C.wordBreak(A,B))
