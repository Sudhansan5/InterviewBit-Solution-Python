class TrieNode:
    def __init__(self):
        self.left=None
        self.right=None
        self.one=0
        self.zero=0

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
                curr.zero+=1
                curr=curr.left
            else:
                if not curr.right:
                    curr.right=TrieNode()
                curr.one+=1
                curr=curr.right

    def query(self,A,B):
        sum=0
        curr=self.root
        for i in range(31,-1,-1):
            if not curr:
                return sum
            b=(A>>i)&1
            c=(B>>i)&1
            if c==1:
                if b==1:
                    sum+=curr.one
                    curr=curr.left
                else:
                    sum+=curr.zero
                    curr=curr.right
            else:
                if b==1:
                    curr=curr.right
                else:
                    curr=curr.left
        return sum

    def Solve(self,A,B):
        self.insert(0)
        pre=0
        sum=0
        for i in A:
            pre ^= i
            sum+=self.query(pre,B)
            self.insert(pre)
            sum %= 1000000007
        return sum

A = [8, 3, 10, 2, 6, 7, 6, 9, 3]
B = 3
C=Solution()
print(C.Solve(A,B))
