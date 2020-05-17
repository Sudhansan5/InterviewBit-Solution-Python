import heapq
class Solution:
    def Solve(self,A,B):
        n=len(A)
        pq=[]
        smallest = A[0]/A[n-1]
        heapq.heappush(pq,(smallest,0,n-1))
        ans=[]
        vis=set()
        vis.add((0,n-1))
        for i in range(B-1):
            global j,k,l,tmp
            while pq:
                j,k,l=heapq.heappop(pq)
                ans.append((A[k],A[l]))
            tmp=(k+1,l)
            if tmp not in vis:
                heapq.heappush(pq,(A[k+1]/A[l],k+1,l))
                vis.add(tmp)
            tmp=(k,l-1)
            if tmp not in vis:
                heapq.heappush(pq,(A[k]/A[l-1],k,l-1))
                vis.add(tmp)
        return ans[B-1]

A=[1,7,11,13,15,17,19]
B=3
C=Solution()
print(C.Solve(A,B))
