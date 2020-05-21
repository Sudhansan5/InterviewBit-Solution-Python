from heapq import *
class Solution:
    def Solve(self,A):
        heapify(A)
        s1,s2=nsmallest(2,A)
        l1,l2,l3=nlargest(3,A)
        return max(s1*s2*l1,l1*l2*l3)

A=[ 0, -1, 3, 100, -70, -50]
B=Solution()
print(B.Solve(A))
