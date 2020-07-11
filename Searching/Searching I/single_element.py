class Solution:
    def Solve(self,A):
        n=len(A)
        ans = -1
        l = 0
        h = n-1
        while l <= h:
            mid = (l+h) // 2
            if mid == n-1:
                return A[n-1]

            if A[mid] == A[mid+1]:
                mid += 1

            if mid % 2 == 1:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1

        return A[ans] if ans != -1 else -1

if __name__ == '__main__':
    A = [1,1,2,2,3]
    B = Solution()
    print(B.Solve(A))
