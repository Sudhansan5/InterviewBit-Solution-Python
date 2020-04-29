class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def lcs(self,A,B,aux):
        if not A:
            return 0
        count=0
        for i in aux:
            if abs(i-A.val) <= B:
                count+=1
        aux.append(A.val)
        count += self.lcs(A.left,B,aux) + self.lcs(A.right,B,aux)
        aux.pop()
        return count

    def Solve(self,A,B):
        return self.lcs(A,B,[])

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
A=2
B=Solution()
print(B.Solve(root,A))
