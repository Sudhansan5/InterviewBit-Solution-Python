class TrieNode:
    def __init__(self):
        self.child={}
        self.terminal=False
        self.count=0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def Solve(self,A):
        for i in A:
            head = self.root
            for j in i:
                if j in head.child:
                    head = head.child[j]
                    head.count+=1
                else:
                    head.child[j] = TrieNode()
                    head = head.child[j]
                    head.count = 1
            head.terminal=True
        ans=[]
        for i in A:
            s=""
            tmp=self.root
            for j in i:
                if j in tmp.child:
                    if tmp.child[j].count > 1:
                        s+=j
                    else:
                        s+=j
                        break
                    tmp=tmp.child[j]
            ans.append(s)
        return ans

A=['zebra', 'dog', 'duck', 'dove']
B=Solution()
print(B.Solve(A))
