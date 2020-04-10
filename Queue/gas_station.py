class Solution:
    def Solve(self,A,B):
        if not A or not B:
            return -1
        start=0
        end=0
        curr=0
        for i in range(len(B)):
            curr += A[i]-B[i]
            end += A[i]-B[i]
            if curr < 0:
                start = i+1
                curr=0
        return start if end >= 0 else -1

A=[1,2,3,4,5]
B=[3,4,5,1,2]
C=Solution()
print(C.Solve(A,B))
