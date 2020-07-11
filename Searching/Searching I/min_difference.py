class Solution:
    def binarySearch(self,A,B):
        l = 0
        h = len(A) - 1
        min_ = float('-inf')
        max_ = float('-inf')

        while l <= h:
            mid = (l + h) // 2
            if A[mid] == B:
                return A[mid], A[mid]
            elif A[mid] < B:
                min_ = max(min_,A[mid])
                l = mid + 1
            elif A[mid] > B:
                max_ = max(max_, A[mid])
                h = mid - 1
        return min_,max_

    def Solve(self,A,B,C):
        for i in C:
            i.sort()
        ans = float('inf')
        for i in range(A-1):
            for j in range(B):
                min_, max_ = self.binarySearch(C[i+1], C[i][j])
                ans = min(ans, abs(C[i][j] - min_), abs(C[i][j] - max_))
        return ans

if __name__ == '__main__':
    A = 3
    B = 2
    C = [[7, 3],
         [2, 1],
         [4, 9]]
    D = Solution()
    print(D.Solve(A,B,C))
