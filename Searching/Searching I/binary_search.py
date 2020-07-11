class Solution:
    def Search(self,A,i,j,B):
        if i >= j:
            return -1
        mid = (i+j)//2
        if mid == B:
            return mid
        elif B < mid:
            return self.Search(A,i,mid-1,B)
        else:
            return self.Search(A,mid+1,j,B)

    def bin_search(self,A,B):
        n=len(A)
        l = 0
        h = n-1
        while l <= h:
            mid = (l+h)//2
            if A[mid] > B:
                h = mid-1
            elif A[mid] < B:
                l = mid + 1
            elif A[mid] == B:
                return mid
        return -1


if __name__ == '__main__':
    A=[1,2,3,3,3,4,5]
    B=3
    C=Solution()
    print(C.Search(A,0,len(A)-1,B))
    print(C.bin_search(A,B))
