class Solution:
    def Solve(self,A):
        n=len(A)
        ans=[0 for _ in range(n)]
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and A[stack[-1]] > A[i]:
                b=stack.pop()
                ans[b]=A[i]
            stack.append(i)
            ans[i]=-1
        return ans

A = [4, 5, 2, 10, 8]
B=Solution()
print(B.Solve(A))
