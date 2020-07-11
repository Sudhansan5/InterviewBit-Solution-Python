class Solution:
    def search(self,A,l,h,B):
        mid = (l+h) // 2
        if A[mid] == B and A[mid-1] < B:
            return mid
        elif A[mid] >= B:
            return self.search(A,l,mid-1,B)
        else:
            if A[mid] < B:
                return self.search(A,mid+1,h,B)

    def Solve(self,A,B):
        n=len(A)
        return self.search(A,0,n-1,B)

if __name__ == '__main__':
    A = [1, 1, 2, 2, 3, 3 ,7]
    C = 3
    B = Solution()
    print(B.Solve(A,C))
