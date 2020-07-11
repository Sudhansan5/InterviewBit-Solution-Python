class Solution:
    def rotatation(self,A,l,h):
        n=len(A)
        mid = (l+h) // 2
        if A[mid] > A[mid+1]:
            return mid
        elif A[mid] > A[n-1]:
            return self.rotatation(A,mid+1,h)
        else:
            if A[mid] <= A[n-1]:
                return self.rotatation(A,l,mid-1)

    def Search(self,A,l,h,B,k):
        n=len(A)
        mid = (l+h) // 2
        if l > h:
            return -1
        if A[(mid+k)%n] == B:
            return (mid+k)%n
        elif A[(mid+k)%n] > B:
            return self.Search(A,l,mid-1,B,k)
        elif A[(mid+k)%n] < B:
            return self.Search(A,mid+1,h,B,k)

    def Solve(self,A,B):
        n=len(A)
        mid = self.rotatation(A,0,n-1)
        return self.Search(A,0,n-1,B,mid+1)

if __name__ == '__main__':
    A = [4, 5, 6, 0, 1, 2, 3]
    B = 4
    C = Solution()
    print(C.Solve(A,B))
