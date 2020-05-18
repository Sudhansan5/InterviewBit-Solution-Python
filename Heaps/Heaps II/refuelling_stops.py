from heapq import heappop, heappush
class Solution:
    def Solve(self,A,B,C,D):
        max_heap=[]
        C.append(A)
        D.append(float('inf'))
        ans=prev=0
        for dist, cap in zip(C,D):
            B-= dist-prev
            while max_heap and B < 0:
                B += -heappop(max_heap)
                ans+=1
            if B < 0:
                return -1
            heappush(max_heap,-cap)
            prev=dist
        return ans

    def solve(self,A,B,C,D): # XXX: DP Solution O(n^2)
        n=len(C)
        dp=[0 for _ in range(n+1)]
        dp[0]=B
        for i,(dist,cap) in enumerate(zip(C,D)):
            for l in range(i,-1,-1):
                if dp[l] >= dist:
                    dp[l+1] = max(dp[l+1],dp[l]+cap)

        for i,j in enumerate(dp):
            if j >= A:
                return i
        return -1

A = 100
B = 10
C = [10, 20, 30, 60]
D = [60, 30, 30, 40]
E=Solution()
print(E.solve(A,B,C,D))
