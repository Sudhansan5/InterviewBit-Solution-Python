class Interval:
    def __init__(self,s,e):
        self.start=s
        self.end=e

class Solution:
    def Solve(self,A, newIntervals):
        A.append(newIntervals)
        A.sort(key=lambda i: i.start)
        n=len(A)
        ans=[]
        ans.append(A[0])
        for i in range(1,n):
            if A[i].start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, A[i].end)
            else:
                ans.append(A[i])
        return ans


if __name__ == '__main__':
    a1=Interval(1,3)
    a2=Interval(6,9)
    A = [a1, a2]
    B=Interval(2,5)
    C=Solution()
    print(C.Solve(A,B))
