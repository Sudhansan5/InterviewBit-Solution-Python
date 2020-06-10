class Solution:
    def Solve(self,A):
        A=list(A)
        n=len(A)
        if n==1:
            return 0
        A.sort()
        max_diff = abs(A[0]-A[1])
        for i in range(1,n-1):
            max_diff = max(max_diff,abs(A[i]-A[i+1]))
        return max_diff

if __name__ == '__main__':
    A=[1,10,5]
    B=Solution()
    print(B.Solve(A))
