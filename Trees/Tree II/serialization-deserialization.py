class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=[]

    def serialization(self,A):
        if not A:
            self.ans.append(str(-1))
            return
        self.ans.append(str(A.val))
        self.serialization(A.left)
        self.serialization(A.right)

    def deserialization(self,A):
        val=int(next(A))
        if val == -1:
            return
        node=Node(val)
        node.left=self.deserialization(A)
        node.right=self.deserialization(A)
        return node

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

    def Solve(self,A):
        self.serialization(A)
        b=' '.join(self.ans)
        vals=iter(b.split())
        c=self.deserialization(vals)
        self.print_node(c)

root=Node(1)
root.left=Node(2)
root.left.right=Node(10)
root.right=Node(3)
root.right.left=Node(4)
root.right.right=Node(5)
root.right.left.left=Node(6)
A=Solution()
print(A.Solve(root))
