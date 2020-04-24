class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None

class Solution:
    def Solve(self,A):
        curr=A
        prev=None
        next=None
        while curr:
            while curr:
                if curr.left:
                    if next:
                        prev.next=curr.left
                    else:
                        next=curr.left
                    prev=curr.left
                if curr.right:
                    if next:
                        prev.next=curr.right
                    else:
                        next=curr.right
                    prev=curr.right
                curr=curr.next
            curr=next
            prev=next=None
        return A

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

root=Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
A=Solution()
b=A.Solve(root)
A.print_node(b)
