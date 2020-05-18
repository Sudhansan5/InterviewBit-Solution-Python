from heapq import heappop, heappush
class Solution:
    def add(self,p,max_pq,min_pq):
        m=len(max_pq)
        n=len(min_pq)
        if m==n:
            heappush(max_pq,-p)
            heappush(min_pq,-heappop(max_pq))
        else:
            heappush(min_pq,p)
            heappush(max_pq,-heappop(min_pq))

    def find_median(self,max_pq,min_pq):
        m=len(max_pq)
        n=len(min_pq)
        if m==n:
            C=heappop(max_pq)
            D=heappop(min_pq)
            heappush(max_pq,C)
            heappush(min_pq,D)
            return (-C+D)/2
        elif m < n:
            C=heappop(min_pq)
            heappush(min_pq,C)
            return C
        else:
            C=heappop(max_pq)
            heappush(max_pq,C)
            return -C

    def check(self,A,max_pq,min_pq):
        n=len(A)
        for i in range(n-1):
            self.add(A[i],max_pq,min_pq)
            med=self.find_median(max_pq,min_pq)
            if med==A[i+1]:
                return 1
        return 0

    def Solve(self,A):
        max_pq=[]
        min_pq=[]
        l=self.check(A,max_pq,min_pq)
        max_pq.clear()
        min_pq.clear()
        A.reverse()
        r=self.check(A,max_pq,min_pq)
        if l or r:
            return 1
        return 0

A=[ 4,6,8,4]
B=Solution()
print(B.Solve(A))
