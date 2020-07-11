class Solution:
    def check(self,A,B,m):
        n = len(A)
        sum_ = 0
        for i in range(m):
            sum_ += A[i]

        if sum_ > B:
            return False

        for i in range(m,n):
            sum_ += A[i] - A[i-m]
            if sum_ > B:
                return False
        return True

    def Solve(self,A,B):
        l = 1
        h = len(A)

        while l <= h:
            mid = (l + h) // 2
            if self.check(A,B,mid):
                l = mid + 1
            else:
                h = mid - 1

        return l - 1


if __name__ == '__main__':
    A=[1,2,3,4,5]
    B=10
    C=Solution()
    print(C.Solve(A,B))
