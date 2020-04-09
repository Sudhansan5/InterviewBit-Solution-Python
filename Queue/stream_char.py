class Solution:
    def Solve(self,A):
        n=len(A)
        q=[]
        freq={}
        for i in range(n):
            if A[i] not in freq:
                freq[A[i]]=1
            else:
                freq[A[i]]+=1
            q.append(A[i])
            if freq[q[0]]==1:
                print(q[0])
            else:
                while q and freq[q[0]] > 1:
                    q.pop(0)
                if q and freq[q[0]]==1:
                    print(q[0])
                else:
                    print(-1)


A="abbcac"
B=Solution()
print(B.Solve(A))
