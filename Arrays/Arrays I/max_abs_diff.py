class Solution:
    def Solve(self,A):
        n=len(A)
        tmp1=[]
        tmp2=[]
        for i in range(n):
            tmp1.append(A[i]+i)
            tmp2.append(A[i]-i)
        max1, min1 = max(tmp1), min(tmp1)
        max2, min2 = max(tmp2), min(tmp2)
        return max(max1-min1, max2-min2)

if __name__ == '__main__':
    A=[3,2,5,1]
    B=Solution()
    print(B.Solve(A))
