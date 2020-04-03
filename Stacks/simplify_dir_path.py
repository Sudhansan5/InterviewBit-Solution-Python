class Solution:
    def Solve(self,A):
        n=len(A)
        stack=[]
        i=0
        while i < n:
            while i < n and A[i] == '/':
                i+=1
            start=i
            while i < n and A[i]  != '/':
                i+=1
            ans=A[start:i]
            if ans == '..':
                if stack:
                    stack.pop()
            elif ans and ans != '.':
                stack.append(ans)
        if not stack:
            return '/'
        return '/'+'/'.join(stack)

A="/home//foo/"
B=Solution()
print(B.Solve(A))
