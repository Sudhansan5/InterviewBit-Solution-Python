class TrieNode:
    def __init__(self):
        self.child={}
        self.terminal=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,w):
        n=len(w)
        head = self.root
        for i in range(n):
            if w[i] in head.child:
                head = head.child[w[i]]
            else:
                head.child[w[i]]=TrieNode()
                head = head.child[w[i]]
        head.terminal = True

    def Search(self,w):
        n=len(w)
        head = self.root
        for i in range(n):
            if w[i] not in head.child:
                return False
            head = head.child[w[i]]
        return True if head.terminal == True else False

A=['apple','app','appie']
B=Trie()
for i in A:
    B.insert(i)
print(B.Search('appl'))
