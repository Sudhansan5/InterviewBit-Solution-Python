class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def Solve(self,A):
        ans=[]
        while A:
            ans.append(A.val)
            A=A.next
        return 1 if ans == ans[::-1] else 0
