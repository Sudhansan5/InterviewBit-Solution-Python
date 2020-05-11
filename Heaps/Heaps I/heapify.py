class Solution:
    def heapify(self,A,i,n):
        largest=i
        l=2*i+1
        r=2*i+2

        if l < n and A[l] > A[largest]:
            largest=l

        if r < n and A[r] > A[largest]:
            largest=r

        if largest != i:
            A[largest],A[i]=A[i],A[largest]
            self.heapify(A,largest,n)

    def Solve(self,A):
        n=len(A)
        index=n//2-1
        for i in range(index,-1,-1):
            self.heapify(A,i,n)
        return A

A=[ 1, 3, 5, 4, 6, 13,  10, 9, 8, 15, 17 ]
B=Solution()
print(B.Solve(A))
