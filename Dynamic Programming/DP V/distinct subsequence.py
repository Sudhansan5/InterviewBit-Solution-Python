class Solution:
    def dp(self,A,index,dp):
        if index == len(A):
            print(dp)
            return

        pick = self.dp(A,index+1,dp+[A[index]])
        dont = self.dp(A,index+1,dp)
        return pick and dont

    def Solve(self,A):
        return self.dp(A,0,[])

if __name__ == '__main__':
    A = 'abc'
    B = Solution()
    print(B.Solve(A))
