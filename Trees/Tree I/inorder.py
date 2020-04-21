class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def inorder(self,root):
        curr=root
        stack=[]
        ans=[]
        while True:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                if not stack:
                    break
                curr=stack.pop()
                ans.append(curr.val)
                curr=curr.right
        return ans


    def inorder_recursive(self,root,aux):
        if not root:
            return
        self.inorder_recursive(root.left,aux)
        aux.append(root.val)
        self.inorder_recursive(root.right,aux)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
B=[]
A.inorder_recursive(root,B)
print(B)
print(A.inorder(root))
