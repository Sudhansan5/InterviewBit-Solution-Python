class Solution:
    def Solve(self,A):
        n=len(A)
        count=0
        orig=1
        for i in range(n):
            if A[i]==0:
                if orig==1:
                    count+=1
                    orig=0
            else:
                if orig==0:
                    count+=1
                    orig=1
        return count

A = [0, 1, 0, 1]
B = Solution()
print(B.Solve(A))
