class Solution:
    def Solve(self,A):
        n=len(A)
        start, end = 0, -1
        _sum, max_sum = 0, 0
        count, maxm = 0, 0
        f_start, f_end = -1, -1
        i = 0
        ans=[]
        while i < n:
            if A[i] >= 0:
                _sum += A[i]
                count += 1
                end += 1

            if _sum > max_sum:
                max_sum = _sum
                f_start = start
                f_end = end

            elif _sum == max_sum and count > maxm:
                maxm = count
                f_start = start
                f_end = end

            if A[i] < 0:
                count = 0
                start = i+1
                end = i
                _sum = 0
            i += 1

        if f_start != -1 and f_end != -1:
            for i in range(f_start, f_end+1):
                ans.append(A[i])
        return ans

if __name__ == '__main__':
    A=[0, 0, -1, 0]
    B=Solution()
    print(B.Solve(A))
