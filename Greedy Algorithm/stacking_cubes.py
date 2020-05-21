class Solution:
    def Solve(self,A):
        count=0
        for i in range(1,A//2+1):
            x=A-i
            if x%i==0:
                count+=1
        return count

A=4
B=Solution()
print(B.Solve(A))
