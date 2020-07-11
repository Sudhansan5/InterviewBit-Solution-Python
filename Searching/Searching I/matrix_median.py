from bisect import *
class Solution:
    def binary_search(self,A, min_el, max_el, cnt_before_mid):
        s = min_el
        e = max_el
        while s < e:
            mid = (s+e) // 2
            count = 0
            for row in A:
                count += bisect_right(row, mid)
            if count > cnt_before_mid:
                e = mid
            else:
                s = mid + 1
        return s

    def Solve(self,A):
        min_el = float('inf')
        max_el = float('-inf')
        for i in A:
            min_el = min(i[0], min_el)
            max_el = max(i[-1], max_el)
        m=len(A)
        n=len(A[0])
        cnt_before_mid = (m*n) // 2
        return self.binary_search(A, min_el, max_el,cnt_before_mid)

if __name__ == '__main__':
    A = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    B = Solution()
    print(B.Solve(A))
