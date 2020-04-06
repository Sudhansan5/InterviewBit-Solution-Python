class Solution:
    def Solve(self,A):
        n=len(A)
        freq={}
        vis={}
        for i in A:
            vis[i]=False
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        ans=[]
        for i in range(n):
            freq[A[i]]-=1
            if vis[A[i]]:
                continue
            while ans and ans[-1] > A[i] and freq[ans[-1]] > 0:
                b=ans.pop()
                vis[b]=False
            ans.append(A[i])
            vis[A[i]]=True
        return ''.join(ans)

A='cbacdcbcd'
B=Solution()
print(B.Solve(A))
