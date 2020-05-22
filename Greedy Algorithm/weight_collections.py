from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph=defaultdict(list)
        self.ans=float('-inf')

    def dfs(self,C,curr,par,k,curr_sum):
        if not k:
            return

        if curr != 1:
            edge_wt = abs(C[curr-1]-C[par-1])
            tmp = curr_sum + (k *edge_wt)
            self.ans = max(self.ans,tmp)
            m=len(self.graph[curr])
            for i in range(m):
                v = self.graph[curr][i]
                self.dfs(C,v,curr,k-1,curr_sum+edge_wt)
        else:
            m=len(self.graph[curr])
            for i in range(m):
                v=self.graph[curr][i]
                self.dfs(C,v,curr,k,curr_sum)

    def Solve(self,A,B,C):
        mod=1000000007
        n=len(B)
        for i in range(n):
            self.graph[B[i]].append(i+1)
        self.dfs(C,1,0,A,0)
        return self.ans%mod

A = 3
B = [0, 1, 1, 2, 2, 3]
C = [1, 6, 7, 21, 5, 18]
D = Solution()
print(D.Solve(A,B,C))
