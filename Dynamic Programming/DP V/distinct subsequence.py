class Solution:
    def dp(self, A, index,aux, dp):
        if index == len(A):
            if aux and aux not in dp:
                dp.add(aux)
            return

        if aux in dp:
            return

        pick = self.dp(A,index+1,aux + A[index],dp)
        dont = self.dp(A,index+1,aux,dp)
        return pick and dont

    def dfs(self, A, index, dp):
        mod = 10 ** 9 + 7
        if index == len(A):
            return 1

        val = self.dfs(A,index+1,dp)
        curr = A[index]

        if curr not in dp:
            dp[curr] = val%mod
            return val*2
        else:
            ans = (val * 2 - dp[curr])
            dp[curr] = val
            return ans%mod

    def Solve(self,A):
        A = [i for i in A]
        dp = {}
        return self.dfs(A,0, dp)-1, dp

if __name__ == '__main__':
    A = 'aaa'
    B = Solution()
    print(B.Solve(A))
