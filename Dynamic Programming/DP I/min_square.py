from math import sqrt, ceil
class Solution:
    def Solve(self,A):
        dp=[0,1,2,3]
        for i in range(4,A+1):
            dp.append(i)
            for j in range(1,int(ceil(sqrt(i)))+1):
                tmp = j*j
                if tmp > i:
                    break
                else:
                    dp[i] = min(dp[i],1+dp[i-tmp])
        return dp[A]

A=6
B=Solution()
print(B.Solve(A))
