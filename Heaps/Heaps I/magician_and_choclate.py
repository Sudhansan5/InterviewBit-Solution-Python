import heapq
class Solution:
    def Solve(self,A,B):
        val=1000000007
        heap=[]
        ans=0
        for i in B:
            heapq.heappush(heap,-i)
        for i in range(A):
            b=(-1)*heapq.heappop(heap)
            ans = (ans + (b%val))%val
            heapq.heappush(heap,int(-b/2))
        return ans
A=10
B=[2147483647, 2000000014, 2147483647]
C=Solution()
print(C.Solve(A,B))
