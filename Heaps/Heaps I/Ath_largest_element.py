import heapq
class Solution:
    def Solve(self,A,B):
        n=len(B)
        ans=[]
        pq=[]
        for i in range(A):
            heapq.heappush(pq,B[i])
            if i < A-1:
                ans.append(-1)
            else:
                x=heapq.heappop(pq)
                ans.append(x)
                heapq.heappush(pq,x)

        for i in range(A,n):
            x=heapq.heappop(pq)
            if B[i] <= x:
                ans.append(x)
                heapq.heappush(pq,x)
            else:
                heapq.heappush(pq,B[i])
                x=heapq.heappop(pq)
                ans.append(x)
                heapq.heappush(pq,x)
        return ans

A=2
B=[15, 20, 99, 1]
C=Solution()
print(C.Solve(A,B))
