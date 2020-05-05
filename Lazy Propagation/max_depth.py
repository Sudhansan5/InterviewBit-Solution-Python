from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph=defaultdict(list)
        self.aux=defaultdict(list)
        self.level=0

    def dfs(self,v,vis,level):
        vis.add(v)
        self.aux[level].append(v)
        self.level=level
        for i in self.graph[v]:
            if i not in vis:
                self.dfs(i,vis,level+1)

    def Solve(self,A,B,C,D,E,F):
        for i,j in zip(B,C):
            self.graph[i-1].append(j-1)
            self.graph[j-1].append(i-1)

        vis=set()
        self.dfs(0,vis,0)
        ans=[]
        for i,j in zip(E,F):
            tmp=[]
            l=i%(self.level+1)
            for k in self.aux[l]:
                if j < D[k]:
                    tmp.append(D[k])
            if tmp:
                ans.append(min(tmp))
            else:
                ans.append(-1)
        return ans

# A = 5
# B = [1, 4, 3, 1]
# C = [5, 2, 4, 4]
# D = [7, 38, 27, 37, 1]
# E = [1, 1, 2]
# F = [32, 18, 26]

A = 3
B = [1, 2]
C = [3, 1]
D = [7, 15, 27]
E = [1, 10, 1]
F = [29, 6, 26]

G=Solution()
print(G.Solve(A,B,C,D,E,F))
