class Solution:
    def reverse(self,A,i):
        j=len(A)-1
        while i < j:
            A[i],A[j] = A[j],A[i]
            i+=1
            j-=1

    def Solve(self,A):
        n=len(A)
        i=n-2
        while i >= 0 and A[i+1] <= A[i]:
            i-=1
        if i >= 0:
            j=n-1
            while j >= 0 and A[j] <= A[i]:
                j-=1
            A[i],A[j] = A[j],A[i]
        self.reverse(A,i+1)
        return A

if __name__ == '__main__':
    A=[1,2,3]
    B=Solution()
    print(B.Solve(A))
