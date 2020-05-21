from heapq import *
class Solution:
    def Solve(self,A,B,C):
        max_pq=[]
        min_pq=[]
        for i in C:
            heappush(max_pq,-i)
            heappush(min_pq,i)
        ans=[0]*2
        while A:
            global seat
            if max_pq:
                b=-heappop(max_pq)
                ans[0] += b
                seat = b
                if seat > 1:
                    heappush(max_pq,-seat+1)

            if min_pq:
                b=heappop(min_pq)
                ans[1] += b
                seat = b
                if seat > 1:
                    heappush(min_pq,seat-1)
            A-=1
        return ans

A = 4
B = 3
C = [2, 1, 1]
D = Solution()
print(D.Solve(A,B,C))
