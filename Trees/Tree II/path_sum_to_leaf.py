class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=[]

    def path_sum(self,root,path,curr_sum,target):
        if not root:
            return
        if not root.left and not root.right and curr_sum+root.val==target:
            self.ans.append(path+[root.val])
        self.path_sum(root.left,path+[root.val],curr_sum+root.val,target)
        self.path_sum(root.right,path+[root.val],curr_sum+root.val,target)

    def Solve(self,A,B):
        self.path_sum(A,[],0,B)
        return self.ans


root=Node(5)
root.left=Node(4)
root.right=Node(8)
root.left.left=Node(11)
root.left.left.left=Node(7)
root.left.left.right=Node(2)
root.right.left=Node(13)
root.right.right=Node(4)
root.right.right.left=Node(5)
root.right.right.right=Node(1)
A=22
B=Solution()
print(B.Solve(root,A))
