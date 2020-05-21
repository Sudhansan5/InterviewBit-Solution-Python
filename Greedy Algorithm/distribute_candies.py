class Solution:
    def Solve(self,A):
        n=len(A)
        candies=[1 for _ in range(n)]
        for i in range(1,n):
            if A[i-1]==A[i]:
                continue
            elif A[i] > A[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1]+1
            else:
                j=i-1
                while j >= 0 and A[j] > A[j+1] and candies[j] <= candies[j+1]:
                    candies[j] = candies[j+1]+1
                    j-=1
        return sum(candies)

A=[1,5,2,1]
B=Solution()
print(B.Solve(A))
