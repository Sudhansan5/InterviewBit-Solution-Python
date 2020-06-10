class Solution:
    def Solve(self,A):
        n=len(A)
        _sum=0
        max_sum=float('-inf')
        for i in range(n):
            _sum += A[i]
            max_sum = max(max_sum,_sum)
            if _sum < 0:
                _sum = 0
        return max_sum

if __name__ == '__main__':
    A=[1,2,4,5,-10]
    B=Solution()
    print(B.Solve(A))
