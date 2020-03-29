from _collections import defaultdict,deque
class Solution:
    def __init__(self):
        self.graph=defaultdict(list)

    def Solve(self,A,B,C):
        for i,j in zip(B,C):
            self.graph[i-1].append(j-1)
        in_degree={}
        for i in range(A):
            in_degree[i]=0
        for i in self.graph:
            for j in self.graph[i]:
                if j not in in_degree:
                    in_degree[j]=1
                else:
                    in_degree[j]+=1
        q=deque()
        for i in in_degree:
            if in_degree[i]==0:
                q.append(i)
        ans=[]
        while q:
            i=q.popleft()
            ans.append(i)
            for j in self.graph[i]:
                in_degree[j]-=1
                if in_degree[j]==0:
                    q.append(j)
        if len(ans)==A:
            return 1
        return 0


A=3
B=[1,2]
C=[2,1]
D=Solution()
print(D.Solve(A,B,C))
