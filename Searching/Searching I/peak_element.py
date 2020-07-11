class Solution:
    def Search(self,A,l,h):
        n=len(A)
        mid = (l+h) // 2
        if mid == 0:
            return A[0]
        if mid == n-1:
            return A[n-1]
        if A[mid] > A[mid-1] and A[mid] >= A[mid+1]:
            return A[mid]
        elif A[mid-1] < A[mid] and A[mid] <= A[mid+1]:
            return self.Search(A,mid+1,h)
        else:
            return self.Search(A,l,mid-1)

    def Solve(self,A):
        n=len(A)
        return self.Search(A,0,n-1)

if __name__ == '__main__':
    A = [1, 1000000000, 1000000000]
    B = Solution()
    print(B.Solve(A))
