import operator
class TrieNode:
    def __init__(self):
        self.child={}
        self.terminal=False

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,A):
        B=A.split('_')
        for i in B:
            head=self.root
            for j in i:
                if j in head.child:
                    head=head.child[j]
                else:
                    head.child[j]=TrieNode()
                    head=head.child[j]
            head.terminal=True

    def count(self,A):
        count=0
        for i in A:
            head=self.root
            for j in i:
                if j in head.child:
                    if head.child[j].terminal:
                        count+=1
                    head=head.child[j]
        return count

    def Solve(self,A,B):
        self.insert(A)
        aux={}
        for i,j in enumerate(B):
            C=j.split('_')
            b=self.count(C)
            aux[i]=b
        sorted_x = sorted(aux.items(), key=operator.itemgetter(1),reverse=True)
        ans=[]
        for i,j in sorted_x:
            ans.append(i)
        return ans

S = "pool_fridge_wifi"
R = ["water_in_pool", "pond_fridge_drink", "pool_wifi_speed"]

A = "cool_ice_wifi"
B = [ "water_is_cool", "cold_ice_drink", "cool_wifi_speed" ]
T=Solution()
print(T.Solve(S,R))
