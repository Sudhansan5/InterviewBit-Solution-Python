class TrieNode:
    def __init__(self):
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,A):
        curr=self.root
        for i in range(31,-1,-1):
            b=(A>>i)&1
            if b==0:
                if not curr.left:
                    curr.left=TrieNode()
                curr=curr.left
            else:
                if not curr.right:
                    curr.right=TrieNode()
                curr=curr.right

    def XOR(self,A):
        curr=self.root
        curr_xor=0
        for i in range(31,-1,-1):
            b=(A>>i)&1
            if b==1:
                if curr.right:
                    curr=curr.right
                else:
                    curr_xor+=pow(2,i)
                    curr=curr.left
            else:
                if curr.left:
                    curr=curr.left
                else:
                    curr_xor+=pow(2,i)
                    curr=curr.right
        return curr_xor

    def Solve(self,A):
        n=len(A)
        min_xor=float('inf')
        self.insert(A[0])
        for i in range(1,n):
            min_xor = min(min_xor,self.XOR(A[i]))
            self.insert(A[i])
        return min_xor

A = [12, 4, 6, 2]
B = Solution()
print(B.Solve(A))
