from heapq import *
class Solution:
    def Solve(self, A, B, C, D):
        pq = [A,B,C]
        heapify(pq)
        ans = []
        while pq:
            tmp = heappop(pq)
            heappush(pq, tmp*A)
            heappush(pq, tmp*B)
            heappush(pq, tmp*C)
            if len(ans) == D:
                return ans
            if tmp not in ans:
                ans.append(tmp)
        return ans

if __name__ == '__main__':
    A = 3
    B = 2
    C = 7
    D = 3
    E = Solution()
    print(E.Solve(A, B,C,D))
