class Solution:
    def paintersReq(self,A,mid):
        total = 0
        numOfPainters = 1
        n = len(A)
        for i in range(n):
            total += A[i]
            if total > mid:
                total = A[i]
                numOfPainters += 1

        return numOfPainters

    def Solve(self,A,B,C):
        l = max(C)
        h = sum(C)

        while l < h:
            mid = (l+h) // 2
            req_painters = self.paintersReq(C,mid)

            if req_painters <= A:
                h = mid
            else:
                l = mid + 1

        return l * B % 10000003


if __name__ == '__main__':
    A = 2
    B = 1
    C = [1, 8, 11, 3]
    D = Solution()
    print(D.Solve(A, B, C))
