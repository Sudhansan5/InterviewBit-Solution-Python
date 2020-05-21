class Solution:
    def Solve(self,A):
        n=len(A)
        ans=[1 for _ in range(n)]
        for i in range(1,n):
            if A[i-1] == A[i]:
                continue
            elif A[i] > A[i-1] and ans[i] <= ans[i-1]:
                ans[i] = ans[i-1]+1
            else:
                j=i-1
                while j > 0 and A[j] > A[j+1] and ans[j] <= ans[j+1]:
                    ans[j] = ans[j+1]+1
                    j-=1
        return sum(ans),ans

A=[1,2,2]
B=Solution()
print(B.Solve(A))
