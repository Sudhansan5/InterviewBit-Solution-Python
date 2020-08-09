class Node:
    def __init__(self,v,w):
        self.val = v
        self.wt = w

class Solution:
    def dp(self, A, index, rSum, dp):
        print(rSum)
        global ans
        if index == 0:
            return rSum

        if dp[index][rSum] != float('inf'):
            return dp[index][rSum]

        if rSum < 0: return float('inf')

        if rSum - A[index-1] >= 0:
            ans = min(self.dp(A,index-1,rSum-A[index-1], dp) + 1, self.dp(A,index-1,rSum,dp))
        else:
            ans = self.dp(A,index-1,rSum,dp)

        dp[index][rSum] = ans
        return ans

    def Solve(self, A):
        n = len(A)
        s = sum(A) // 2
        dp = [[float('inf')]*(s+1) for _ in range(n+1)]
        return self.dp(A, n, s, dp),dp

    def flipArray(self, A):
        n = len(A)
        s = sum(A) // 2
        dp = [[Node(0,0)]*(s+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,s+1):
                prev_val = dp[i-1][j].val
                prev_wt = dp[i-1][j].wt

                if j - A[i-1] >= 0:
                    curr_wt = dp[i-1][j-A[i-1]].wt + A[i-1]
                    curr_val = dp[i-1][j-A[i-1]].val + 1

                    if (curr_wt > prev_wt) or (curr_wt == prev_wt and curr_val < prev_val):
                        dp[i][j] = Node(curr_val,curr_wt)
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][s].val

if __name__ == '__main__':
    A = [9,16]
    B = Solution()
    #print(B.Solve(A))
    print(B.flipArray(A))
