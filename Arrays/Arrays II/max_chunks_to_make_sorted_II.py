class Solution:
    def Solve(self,A):
        n=len(A)
        B=sorted(A)
        sum_1=0
        sum_2=0
        ans=0
        for i in range(n):
            sum_1 += A[i]
            sum_2 += B[i]
            if sum_1==sum_2:
                ans += 1
        return ans
        
if __name__ == '__main__':
    A=[2,0,1,2]
    B=Solution()
    print(B.Solve(A))
