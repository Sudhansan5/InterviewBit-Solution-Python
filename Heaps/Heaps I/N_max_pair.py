import heapq
class Solution:
    def Solve(self,A,B):
        n=len(A)
        A=sorted(A)
        B=sorted(B)
        heap=[]
        indices=set()
        heapq.heappush(heap,(-(A[n-1]+B[n-1]),(n-1,n-1)))
        indices.add((n-1,n-1))
        ans=[]
        for _ in range(n):
            i,(j,k) = heapq.heappop(heap)
            ans.append(-1*i)
            global sums
            global tmp
            if  j >= 1:
                sums = A[j-1]+B[k]
                tmp=(j-1,k)
                if tmp not in indices:
                    heapq.heappush(heap,(-sums,tmp))
                    indices.add(tmp)
            if k >= 1:
                sums=A[j]+B[k-1]
                tmp=(j,k-1)
                if tmp not in indices:
                    heapq.heappush(heap,(-sums,tmp))
                    indices.add(tmp)
        return ans

A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C=Solution()
print(C.Solve(A,B))
