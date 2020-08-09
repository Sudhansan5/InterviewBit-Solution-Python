class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dp(self,A):
        if not A:
            return 0

        l = max(0,self.dp(A.left))
        r = max(0,self.dp(A.right))

        self.ans = max(self.ans, l + A.val + r)
        return max(l,r,0) + A.val


    def Solve(self, A):
        self.ans = float('-inf')
        self.dp(A)
        return self.ans

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    A = Solution()
    print(A.Solve(root))
