class Solution:
    def Solve(self,A):
        n=len(A)
        stack=[-1]
        ans=0
        for i in range(n):
            if A[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, i-stack[-1])
                else:
                    stack.append(i)
        return ans

A=")()())"
B=Solution()
print(B.Solve(A))
