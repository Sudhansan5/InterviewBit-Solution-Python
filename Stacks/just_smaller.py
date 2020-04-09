class Solution:
    def Solve(self,A):
        n=len(A)
        ans=[0 for _ in range(n)]
        stack=[]
        for i in range(n):
            while stack and A[i] < A[stack[-1]]:
                b=stack.pop()
                ans[b]=A[i]
            stack.append(i)
            ans[i]=-1
        return ans

A=[1]
B=Solution()
print(B.Solve(A))
