class Solution:
    def Solve(self,A,B):
        n=len(B)
        ans = 0
        i=0
        while i <= n:
            ans += B[i]
            if ans >= A:
                return i+1
            elif i == n-1 and ans < A:
                i=-1
            i+=1

if __name__ == '__main__':
    A=1000
    B=[100, 100, 100, 100, 100, 100, 100]
    C=Solution()
    print(C.Solve(A,B))
