class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def find_height(self,A):
        if not A:
            return 0
        else:
            ht1=self.find_height(A.left)
            ht2=self.find_height(A.right)
            if ht1 > ht2:
                return ht1+1
            else:
                return ht2+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
print(A.find_height(root))
