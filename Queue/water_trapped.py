class Solution:
    def Solve(self,A):
        n=len(A)
        pre=[0 for _ in range(n)]
        post=[0 for _ in range(n)]
        ans=0
        pre[0]=A[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],A[i])
        post[-1]=A[-1]
        for j in range(n-2,-1,-1):
            post[j]=max(post[j+1],A[j])
        for k in range(n):
            ans+= min(pre[k],post[k])-A[k]
        return ans

A=[0,1,0,2,1,0,1,3,2,1,2,1]
B=Solution()
print(B.Solve(A))
