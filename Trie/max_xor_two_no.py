class TrieNode:
    def __init__(self):
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,A):
        n=len(A)
        for i in range(n):
            head=self.root
            for j in range(31,-1,-1):
                b=(A[i]>>j)&1
                if b==0:
                    if not head.left:
                        head.left=TrieNode()
                    head=head.left
                else:
                    if not head.right:
                        head.right=TrieNode()
                    head = head.right

    def find_xor(self,A):
        n=len(A)
        max_xor=float('-inf')
        for i in range(n):
            curr = self.root
            curr_xor=0
            val=A[i]
            for j in range(31,-1,-1):
                b=(val>>j)&1
                if b==1:
                    if curr.left:
                        curr_xor += pow(2,j)
                        curr=curr.left
                    else:
                        curr=curr.right
                else:
                    if curr.right:
                        curr_xor += pow(2,j)
                        curr=curr.right
                    else:
                        curr=curr.left
            max_xor=max(max_xor,curr_xor)
        del self.root
        return max_xor

    def Solve(self,A):
        self.insert(A)
        return self.find_xor(A)

A=[1,2,3,4,5]
B=Solution()
print(B.Solve(A))
