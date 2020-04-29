class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def traverse(self,A):
        if not A:
            return
        A.val=0
        self.traverse(A.left)
        self.traverse(A.right)

    def find_vertex(self,A):
        if not A:
            return 0
        if not A.left and not A.right:
            return 0
        if A.val != 0:
            return A.val

        s1 = 1 + self.find_vertex(A.left) + self.find_vertex(A.right)
        s2 = 0

        if A.left:
            s2 += 1 + self.find_vertex(A.left.left) + self.find_vertex(A.left.right)
            
        if A.right:
            s2 += 1 + self.find_vertex(A.right.left) + self.find_vertex(A.right.right)

        A.val = min(s1,s2)
        return A.val

    def Solve(self,A):
        self.traverse(A)
        return self.find_vertex(A)

root = Node(9)
root.left = Node(6)
root.right = Node(17)
root.left.left = Node(23)
root.left.right = Node(7)

A=Solution()
print(A.Solve(root))
